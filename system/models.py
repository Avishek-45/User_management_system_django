from django.db import models

# Create your models here.

class customer(models.Model):
    name=models.CharField(max_length=100,null=True)
    phone=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    date_created=models.TimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
    )

    name=models.CharField(max_length=100,null=True)
    price=models.FloatField()
    category=models.CharField(max_length=100,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.TimeField(auto_now_add=True,null=True)
    tags=models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    Customer=models.ForeignKey(customer,null=True,on_delete=models.SET_NULL)
    Products=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    Status=models.CharField(max_length=100,null=True,choices=STATUS)
    date_created=models.TimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.Products.name


