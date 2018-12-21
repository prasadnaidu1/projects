from django.db import models
class addstate(models.Model):
    id=models.IntegerField(primary_key=True)
    state=models.CharField(max_length=50)

class addscity(models.Model):
    id=models.IntegerField(primary_key=True)
    Add_state= models.ForeignKey(addstate, on_delete=models.CASCADE)
    city=models.CharField(max_length=50)

class donor(models.Model):
    name=models.CharField(max_length=50)   
    cno=models.IntegerField()
    city=models.ForeignKey(addscity,on_delete=models.CASCADE)
    email=models.EmailField(primary_key=True)
    password=models.IntegerField()
class organisation(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField()
    city=models.ForeignKey(addscity,on_delete=models.CASCADE)
    email=models.EmailField(primary_key=True)
    password=models.IntegerField()
class suggetions(models.Model):
    message=models.CharField(max_length=50)



