from datetime import datetime
from django.db import models
from django.db.models.deletion import CASCADE
# Create your models here.

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=15,default='')
    email=models.EmailField(default='')
    password=models.CharField(max_length=8,default='')

    def __str__(self):
        return self.username

class type(models.Model):
    cleaning_type=models.CharField(max_length=20,default='')

    def __str__(self):
        return self.cleaning_type

class clean(models.Model):
    
    Category=models.ForeignKey(type,on_delete=models.CASCADE)
    title=models.CharField(max_length=25,default='')
    img=models.ImageField(upload_to='media',blank=True,default=None)
    price=models.PositiveIntegerField(default=None)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title      

class mycart(models.Model):

    person=models.ForeignKey(user,on_delete=CASCADE)
    serv=models.ForeignKey(clean,on_delete=CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(null=True)

    def __str__(self):
        return self.serv.title

class orders(models.Model):

    order_id=models.AutoField(primary_key=True)
    oemail=models.EmailField(default='')
    name=models.CharField(max_length=25,default='')
    services=models.CharField(max_length=500,default='')
    adddress=models.CharField(max_length=200,default='')
    contact=models.CharField(max_length=11,default='')
    service_date=models.DateField(auto_now_add=False)
    amount=models.PositiveIntegerField(default=None)
    placed_at=models.DateTimeField(auto_now_add=False,default=datetime.now())

    def __str__(self) -> str:
        return self.services

