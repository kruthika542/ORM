from django.db import models
from django.contrib import admin
class car(models.Model):
    cid=models.IntegerField()
    brandname=models.CharField(max_length=100)
    collection=models.IntegerField()
    price=models.IntegerField()
    rating=models.FloatField()

class carAdmin(admin.ModelAdmin):
    list_display=('cid','brandname','collection','price','rating')
