from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(models.Model):
    stock = models.PositiveIntegerField(_("product stock count"), default=0)
    category = models.CharField(_("product category"), max_length=20)
    price = models.PositiveIntegerField(_("product price"))
    name = models.CharField(_("product name"), max_length=255)
    description = models.CharField(_("product description"), max_length=2000)
    sell = models.PositiveIntegerField(_("sell count"), default=0)

    class Meta:
        unique_together = ("category", "name")
