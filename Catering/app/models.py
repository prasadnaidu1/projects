from django.db import models

class userregisteration(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    email=models.EmailField(primary_key=True)
    add=models.CharField(max_length=500)
    username=models.CharField(max_length=12)
    password=models.IntegerField(default=10)
class Functiondetails(models.Model):
    fun=models.CharField(max_length=50)
class veg150(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class veg200(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate=models.CharField(max_length=20)
class veg300(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class veg350(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class veg400(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class NOnveg150(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class Nonveg200(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class Nonveg300(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class Nonveg350(models.Model):
    item_id=models.IntegerField(primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class Nonveg400(models.Model):
    item_id=models.IntegerField(default=5,primary_key=True)
    item_name=models.CharField(max_length=50)
    item_type=models.CharField(max_length=50)
    item_plate = models.CharField(max_length=20)
class swetdetails(models.Model):
    sweet=models.CharField(max_length=50)
class orderdetail(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField()
    d_add=models.CharField(max_length=500)
    food_type=models.CharField(max_length=50)
    d_date=models.DateField()
    no_plates=models.IntegerField()



