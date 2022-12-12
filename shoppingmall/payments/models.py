from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import User
from products.models import Product


# Create your models here.
class Payment(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("buyer of payment"))
    amount = models.PositiveBigIntegerField(_("amount of payment"))


class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))
    quantity = models.PositiveSmallIntegerField(_("quantity"))

