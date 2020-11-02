from django.db import models

# Create your models here.
class Query(models.Model):
    name = models.CharField(max_length=122)
    bookname = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=122)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name1 = models.CharField(max_length=122)
    phone1 = models.CharField(max_length=12)
    email1 = models.CharField(max_length=122)
    desc1 = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.name1

class Product(models.Model):
    product_id =models.AutoField
    product_name =models.CharField(max_length=50)
    catagory=models.CharField(max_length=50,default="")
    subcatagory = models.CharField(max_length=50,default="")
    mainprice = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    Author=models.CharField(max_length=50,default="")
    desc2=models.CharField(max_length=5000,default="")
    pub_date=models.DateField()
    image = models.ImageField(upload_to="static/images",default="")
    
    def __str__(self):
        return self.product_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json =models.CharField(max_length=5000)
    name2 = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone2 = models.CharField(max_length=12)
    
    def __str__(self):
        return self.items_json

class OrdersUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc
