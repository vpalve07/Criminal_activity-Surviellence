# from home.views import contact
from django.db import models
from django.db.models.expressions import Value

# Create your models here.

'''
class User(models.Model):
    email = models.EmailField(max_length=122)
    password = models.CharField(max_length=12,null=False, blank=True, default=00000)
    address = models.TextField(max_length=500)
    address2 = models.TextField(max_length=500,default='address')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.IntegerField(max_length=5, null=False, blank=True, default=00000)
    date = models.DateField()
'''
# class sign_up(models.Model):
#     email = models.EmailField(max_length=122)
#     password = models.CharField(max_length=122)

'''class Ex(models.Model):
    email = models.EmailField(max_length=122)
    text = models.TextField()
'''
class User(models.Model):
    email = models.CharField(max_length=122,null=True)
    password = models.CharField(max_length=12,null=True)
    address = models.TextField(null=True)
    address2 = models.TextField(null=True)
    city = models.TextField(null=True)
    zip = models.IntegerField(null=True)


class Officers(models.Model):
    name1 = models.CharField(max_length=122,null=True)
    name2 = models.CharField(max_length=122,null=True)
    email1 = models.CharField(max_length=122,null=True)
    password1 = models.CharField(max_length=12,null=True)
    contact1 = models.IntegerField(null=True)
    rank1 = models.CharField(max_length=122,null=True)
    uniq1 = models.IntegerField(null=True)
    address01 = models.TextField(null=True)
    address02 = models.TextField(null=True)
    city1 = models.TextField(null=True)
    #zip1 = models.IntegerField(null=True)

class Other(models.Model):
    name11 = models.CharField(max_length=122,null=True)
    name22 = models.CharField(max_length=122,null=True)
    email11 = models.CharField(max_length=122,null=True)
    password11 = models.CharField(max_length=12,null=True)
    contact11 = models.IntegerField(null=True)
    pro11 = models.CharField(max_length=122,null=True)
    uniq11 = models.IntegerField(null=True)
    address11 = models.TextField(null=True)
    address22 = models.TextField(null=True)
    city11 = models.TextField(null=True)
    #zip11 = models.IntegerField(null=True)


class Add_Criminal(models.Model):
    fname = models.CharField(max_length=122,null=True)
    lname = models.CharField(max_length=122,null=True)
    age = models.IntegerField(max_length=3,null=True)
    charges = models.CharField(max_length=122,null=True)
    city = models.CharField(max_length=122,null=True)
    zip = models.IntegerField(max_length=122,null=True)
    duration = models.CharField(max_length=122,null=True)
    uniq1 = models.IntegerField(null=True)
    location = models.CharField(max_length=122,null=True)
    image = models.ImageField(upload_to = "static/images")
    status = models.CharField(max_length=122,null=True)
    fname1 = models.CharField(max_length=122,null=True)
    lname1 = models.CharField(max_length=122,null=True)
    age1 = models.IntegerField(null=True)
    rank = models.CharField(max_length=122,null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.fname
    

class Reports(models.Model):
    fname = models.CharField(max_length=122,null=True)
    lname = models.CharField(max_length=122,null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=122,null=True)
    state = models.CharField(max_length=122,null=True)
    zip = models.IntegerField(max_length=122,null=True)
    complaint = models.TextField(max_length=10000,null=True)

    def __str__(self):
        return self.fname

class Search_Name(models.Model):
    ufname = models.CharField(max_length=122,null=True)
    ulname = models.CharField(max_length=122,null=True)
    username = models.EmailField(max_length=122,null=True)
    phone = models.IntegerField(null=True)
    city = models.CharField(max_length=122,null=True)
    cfname = models.CharField(max_length=122,null=True)
    clname = models.CharField(max_length=122,null=True)
    reason = models.CharField(max_length=10000,null=True)

    def __str__(self):
        return self.ufname


class ID(models.Model):
    image1 = models.ImageField(upload_to = "static/images")


class PASP(models.Model):
    fname = models.CharField(max_length=122,null=True)
    lname = models.CharField(max_length=122,null=True)
    age = models.IntegerField(max_length=3,null=True)
    charges = models.CharField(max_length=122,null=True)
    city = models.CharField(max_length=122,null=True)
    zip = models.IntegerField(max_length=122,null=True)
    duration = models.CharField(max_length=122,null=True)
    uniq1 = models.IntegerField(null=True)
    location = models.CharField(max_length=122,null=True)
    image = models.ImageField(upload_to = "static/images")
    status = models.CharField(max_length=122,null=True)
    fname1 = models.CharField(max_length=122,null=True)
    lname1 = models.CharField(max_length=122,null=True)
    age1 = models.IntegerField(null=True)
    rank = models.CharField(max_length=122,null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.fname

class PDCP(models.Model):
    fname = models.CharField(max_length=122,null=True)
    lname = models.CharField(max_length=122,null=True)
    age = models.IntegerField(max_length=3,null=True)
    charges = models.CharField(max_length=122,null=True)
    city = models.CharField(max_length=122,null=True)
    zip = models.IntegerField(max_length=122,null=True)
    duration = models.CharField(max_length=122,null=True)
    uniq1 = models.IntegerField(null=True)
    location = models.CharField(max_length=122,null=True)
    image = models.ImageField(upload_to = "static/images")
    status = models.CharField(max_length=122,null=True)
    fname1 = models.CharField(max_length=122,null=True)
    lname1 = models.CharField(max_length=122,null=True)
    age1 = models.IntegerField(null=True)
    rank = models.CharField(max_length=122,null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.fname

class PIGP(models.Model):
    fname = models.CharField(max_length=122,null=True)
    lname = models.CharField(max_length=122,null=True)
    age = models.IntegerField(max_length=3,null=True)
    charges = models.CharField(max_length=122,null=True)
    city = models.CharField(max_length=122,null=True)
    zip = models.IntegerField(max_length=122,null=True)
    duration = models.CharField(max_length=122,null=True)
    uniq1 = models.IntegerField(null=True)
    location = models.CharField(max_length=122,null=True)
    image = models.ImageField(upload_to = "static/images")
    status = models.CharField(max_length=122,null=True)
    fname1 = models.CharField(max_length=122,null=True)
    lname1 = models.CharField(max_length=122,null=True)
    age1 = models.IntegerField(null=True)
    rank = models.CharField(max_length=122,null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.fname

class PIP(models.Model):
    fname = models.CharField(max_length=122,null=True)
    lname = models.CharField(max_length=122,null=True)
    age = models.IntegerField(max_length=3,null=True)
    charges = models.CharField(max_length=122,null=True)
    city = models.CharField(max_length=122,null=True)
    zip = models.IntegerField(max_length=122,null=True)
    duration = models.CharField(max_length=122,null=True)
    uniq1 = models.IntegerField(null=True)
    location = models.CharField(max_length=122,null=True)
    image = models.ImageField(upload_to = "static/images")
    status = models.CharField(max_length=122,null=True)
    fname1 = models.CharField(max_length=122,null=True)
    lname1 = models.CharField(max_length=122,null=True)
    age1 = models.IntegerField(null=True)
    rank = models.CharField(max_length=122,null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.fname

class PSIP(models.Model):
    fname = models.CharField(max_length=122,null=True)
    lname = models.CharField(max_length=122,null=True)
    age = models.IntegerField(max_length=3,null=True)
    charges = models.CharField(max_length=122,null=True)
    city = models.CharField(max_length=122,null=True)
    zip = models.IntegerField(max_length=122,null=True)
    duration = models.CharField(max_length=122,null=True)
    uniq1 = models.IntegerField(null=True)
    location = models.CharField(max_length=122,null=True)
    image = models.ImageField(upload_to = "static/images")
    status = models.CharField(max_length=122,null=True)
    fname1 = models.CharField(max_length=122,null=True)
    lname1 = models.CharField(max_length=122,null=True)
    age1 = models.IntegerField(null=True)
    rank = models.CharField(max_length=122,null=True)
    phone = models.IntegerField(null=True)

    def __str__(self):
        return self.fname

