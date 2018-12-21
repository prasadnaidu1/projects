from django.db import models

class addstate(models.Model):
    id=models.IntegerField(default=6,primary_key=True)
    state=models.CharField(max_length=50)

class addcity(models.Model):
    id=models.IntegerField(default=6,primary_key=True)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    Addstate=models.ForeignKey(addstate,on_delete=models.CASCADE)

class Adddonor(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    email=models.EmailField(primary_key=True)
    password=models.IntegerField(default=12)

class Addorg(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    email=models.EmailField(primary_key=True)
    password=models.IntegerField(default=12)

class suggetions(models.Model):
    sug=models.CharField(max_length=50)
    choice=models.CharField(max_length=50)


