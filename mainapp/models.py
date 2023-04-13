from django.db import models

class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    addressline1 = models.CharField(max_length=50)
    addressline2 = models.CharField(max_length=50)
    addressline3 = models.CharField(max_length=50)
    pin = models.CharField(max_length=10)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pic = models.ImageField(upload_to="user")
    otp = models.IntegerField(default=-121212)

class Maincategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

class Subcategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,unique=True)
    pic = models.ImageField(upload_to="brand")

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    maincategory = models.ForeignKey(Maincategory,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    baseprice = models.IntegerField()
    discount = models.IntegerField()
    finalprice = models.IntegerField()
    stock = models.BooleanField(default=True)
    description = models.TextField()
    pic1 = models.ImageField(upload_to="product")
    pic2 = models.ImageField(upload_to="product",default="",blank=True,null=True)
    pic3 = models.ImageField(upload_to="product",default="",blank=True,null=True)
    pic4 = models.ImageField(upload_to="product",default="",blank=True,null=True)

    def __str__(self):
        return self.name

status = ((0,"Order Placed"),(1,"Not Packed"),(2,"Packed"),(3,"Ready to Ship"),(4,"Shipped"),(5,"Out For Delivery"),(6,"Delivered"),(7,"Cancelled"))
payment = ((0,"Pending"),(1,"Done"))
mode = ((0,"COD"),(1,"Net Banking"))
class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer,on_delete=models.CASCADE)
    total = models.IntegerField()
    shipping = models.IntegerField()
    final = models.IntegerField()
    rppid = models.CharField(max_length=30,default="",null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    paymentmode = models.IntegerField(choices=mode,default=0)
    paymentstatus = models.IntegerField(choices=payment,default=0)
    orderstatus = models.IntegerField(choices=status,default=0)

    def __str__(self):
        return str(self.id)+" "+self.user.username

class CheckoutProducts(models.Model):
    id = models.AutoField(primary_key=True)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    p = models.ForeignKey(Product,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+str(self.checkout.id)

conatctstatus = ((0,"Active"),(1,"Done"))
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    status = models.IntegerField(choices=conatctstatus,default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.name+" "+self.subject

