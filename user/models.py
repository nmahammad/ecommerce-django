# from itertools import count, product
# from django.db import models
# from django.contrib.auth import get_user_model
# from core.models import AbstractModel
# from product.models import Product, ProductVersion

# # Create your models here.


# User = get_user_model()


# class Basket(AbstractModel):
#     user_id = models.ForeignKey(User, on_delete = models.CASCADE )
#     total_basket_price = models.FloatField(max_length = 50)


# class BasketItem(AbstractModel):
#     quantity =  models.IntegerField()
#     product_version_id = models.ForeignKey(ProductVersion, on_delete = models.CASCADE )
#     basket_id = models.ForeignKey(Basket, on_delete = models.CASCADE)
#     subtotal = models.IntegerField
#     total = models.IntegerField


# class WishList(AbstractModel):
#     product_id = models.ForeignKey(Product, on_delete = models.CASCADE )
#     user_id = models.ForeignKey(User, on_delete = models.CASCADE )


from itertools import count, product
from django.db import models
from django.contrib.auth import get_user_model
from core.models import AbstractModel
from product.models import Product, ProductVersion

# Create your models here.
User = get_user_model()

class Basket(AbstractModel):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE )  
    total_basket_price = models.FloatField(max_length = 50)

class BasketItem(AbstractModel):
    quantity =  models.IntegerField()
    product_version_id = models.ForeignKey(ProductVersion, on_delete = models.CASCADE ) 
    basket_id = models.ForeignKey(Basket, on_delete = models.CASCADE)
    subtotal = models.IntegerField
    total = models.IntegerField



