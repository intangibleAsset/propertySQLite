from django.db import models

# Create your models here.
class Item(models.Model):
    propertyReference = models.CharField(max_length=20)
    createdDate = models.DateTimeField(auto_now_add=True)
    seizedDate = models.DateField()
    seizedTime = models.TimeField()
    description = models.CharField(max_length=20)
    notes = models.TextField()
    #ForeignKeys
    locationRecovered = models.CharField(max_length=20)
    recoveredBy = models.CharField(max_length=20)
    images = models.CharField(max_length=20)
    owner = models.CharField(max_length=20)
    operation = models.CharField(max_length=20)
