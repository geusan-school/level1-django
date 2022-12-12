from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from products.models import Product
from payments.models import Payment, PaymentItem
from payments.serializers import PurchaseSerializer
from drf_spectacular.utils import extend_schema
from operator import itemgetter

# Create your views here.
@extend_schema(
    request=PurchaseSerializer(many=True),
)
@api_view(["post"])
def purchase(request):
    user = request.user
    amount = 0
    # 1. 결제 가능한 지 검사(매진 된 상품이 있는 지)
    serializer = PurchaseSerializer(data=request.data, many=True)
    serializer.is_valid(raise_exception=True)

    queryset = Q()
    for item in serializer.validated_data:
        queryset = queryset | Q(id=item['product_id'], stock__gte=item['quantity'])
    
    products = list(Product.objects.filter(queryset).order_by('id'))
    if len(serializer.validated_data) != len(products):
        raise ValidationError("1 or more items sold out")

    # 2. 스톡 정보 업데이트
    sorted_data = list(sorted(serializer.validated_data, key=itemgetter("product_id")))
    payment_items = []
    for item, product in zip(sorted_data, products):
        product.quantity -= item['quantity']
        product.sell += item['quantity']
        amount += product.price * item['quantity']
        product.save(update_fields=['quantity', 'sell'])
        payment_items.append(PaymentItem(product=product, quantity=item['quantity']))

    # 3. 결제 생성
    payment = Payment.objects.create(
        buyer=user,
        amount=amount
    )
    for item in payment_items:
        item.payment = payment
    PaymentItem.objects.bulk_create(payment_items)

    return Response({ "status": "success", "payment_id": payment.id })
