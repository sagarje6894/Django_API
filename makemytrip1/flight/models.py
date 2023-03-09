from django.db import models


# Create your models here.
class Flight_details(models.Model):
    #fid = models.IntegerField(primary_key=True)
    fname=models.CharField(max_length=20)
    fdate = models.DateField()
    ffare = models.FloatField()
    fstart = models.CharField(max_length=20)
    fend = models.CharField(max_length=20)