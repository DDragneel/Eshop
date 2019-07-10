from django.db import models
from django.contrib.auth.forms import User

class Brand(models.Model):
    bid=models.AutoField
    bname=models.CharField(max_length=30)
    def __str__(self):
        return self.bname

class Category(models.Model):
    cid=models.AutoField
    cname=models.CharField(max_length=30)
    def __str__(self):
        return self.cname
class Product(models.Model):
    id=models.AutoField
    cat=models.ForeignKey(Category,on_delete="CASCADE",default=None)
    name=models.CharField(max_length=30)
    description=models.TextField()
    brand=models.ForeignKey(Brand,on_delete="CASCADE",default=None)
    basicPrice=models.IntegerField()
    discount=models.IntegerField()
    price=models.IntegerField()
    color=models.CharField(max_length=20)
    img1=models.ImageField(upload_to='images')
    img2 = models.ImageField(upload_to='images',default=None)
    img3 = models.ImageField(upload_to='images',default=None)
    img4 = models.ImageField(upload_to='images',default=None)
    date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    cartid=models.AutoField
    cart_user=models.ForeignKey(User,on_delete='CASCADE',default=None)
    cart_product=models.ForeignKey(Product,on_delete='CASCADE',default=None)
    count=models.IntegerField()
    total=models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.cart_user)

class Checkout(models.Model):
    checkid=models.AutoField
    chname=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=50)
    state=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    pin=models.CharField(max_length=10)

    def __str__(self):
        return self.chname
