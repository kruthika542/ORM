# Ex02 Django ORM Web Application
## Date: 19.09.25

## AIM
To develop a Django application to store and retrieve data from a Cars Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
~~~
admin.py

from django.contrib import admin
from .models import car,carAdmin
admin.site.register(car,carAdmin)

models.py

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


~~~


## output
![alt text](<Screenshot 2025-09-19 115535.png>)





## RESULT
Thus the program for creating Cars database using ORM hass been executed successfully
