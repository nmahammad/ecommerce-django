from itertools import product
from django.db import models
import django
from django.forms import ModelForm
# Create your models here.
from core.models import AbstractModel
from product.models import User, Product, ProductVersion
from user.models import Basket, User


class BillingDetail(AbstractModel):
    first_name = models.CharField('name', max_length=50)
    last_name = models.CharField('surname', max_length=50)
    email = models.EmailField('e-mail', max_length=30)
    phone_number = models.CharField('mobile number', max_length=200)

    country_choices = (
        ('1', 'India'),
        ('2', 'South Africa'),
        ('3', 'United States'),
        ('4', 'Australia')

    )

    country = models.TextField('Country', choices=country_choices)
    city_town = models.CharField(
        'City/Town', max_length=50, help_text="City/Town")
    address = models.CharField(
        'Address', max_length=150, help_text="Street Address")
    state = models.CharField('State/Country', max_length=50)
    postal_code = models.CharField('Postal Code', max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.country


class Order(AbstractModel):
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE)
    total_payment = models.FloatField('total payment for order', max_length=50)



class Cart(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.first_name + ' ' + self.owner.last_name + ' ' + str(self.owner.id)
    
    @property
    def grandtotal(self):
        items = self.cart_items.all()
        total = sum([item.subtotal for item in items])
        return total

    @property
    def cartquantity(self):
        items = self.cart_items.all()
        total = sum([item.quantity for item in items])
        return total




class CartItem(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField('quantity')    
    product_version_id = models.ForeignKey(ProductVersion, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_version_id.title + ' ' + str(self.quantity)

    @property
    def subtotal(self):
        return self.quantity * self.product_version_id.price

 

class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete = models.SET_NULL, null=True)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' ' + str(self.user.id)

    @property
    def price(self):
        return (self.product.price)

    @property
    def amount(self):
        return (self.quantity * self.product.price)

    
class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']


