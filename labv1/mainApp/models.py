from django.db import models
from django.utils import timezone

class SampleIntake(models.Model):

    Default_Id = models.AutoField(primary_key=True)
    Date = models.DateField(blank=True, null=True)
    CurrentDate = models.DateField(default=timezone.now)
    SampleId = models.CharField(max_length=128,blank=True, null=True, unique=True)
    SampleName = models.CharField(max_length=128,blank=True, null=True)
    Matrix = models.CharField(max_length=128,blank=True, null=True)
    BatchNumber = models.CharField(max_length=128,blank=True, null=True)
    SampleSize = models.CharField(max_length=128,blank=True, null=True)
    BatchSize = models.CharField(max_length=128,blank=True, null=True)
    DistributorName = models.CharField(max_length=128,blank=True, null=True)
    DistributorLicence = models.CharField(max_length=128,blank=True, null=True)
    CustodyNumber = models.CharField(max_length=128,blank=True, null=True)

    def __str__(self):
        return str(self.SampleId)