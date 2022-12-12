from rest_framework import serializers
from payments.models import PaymentItem


class PurchaseSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = PaymentItem
        fields = ("product", "product_id", "quantity", "payment")
        read_only_fields = ("payment", "product",)
