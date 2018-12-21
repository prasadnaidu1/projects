from django.db import models

class adddoctor(models.Model):
    name=models.CharField(max_length=50)
    cno=models.IntegerField(default=10)
    email=models.EmailField(primary_key=True)
    password=models.IntegerField(default=12)
    exp=models.DecimalField(max_digits=2,decimal_places=2)
    dept=models.CharField(max_length=50)

