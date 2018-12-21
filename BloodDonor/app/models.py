from django.db import models


class addcity(models.Model):
    id=models.IntegerField(default=6,primary_key=True)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
class addstate(models.Model):
    id=models.IntegerField(default=5,primary_key=True)
    name=models.CharField(max_length=50)
    #Addstate = models.ForeignKey(addcity, on_delete=models.CASCADE)
