# Ex02 Django ORM Web Application
## Date: 8.9.2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



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
```
admin.py

from django.contrib import admin
from .models import owner,ownerAdmin
admin.site.register(owner,ownerAdmin)

models.py

from django.db import models
from django.contrib import admin
class owner (models.Model):
    Model=models.CharField(max_length=10)
    Car_no=models.IntegerField(primary_key=True)
    Quality=models.CharField(max_length=10)
    Year_prod=models.IntegerField()
    Colour=models.CharField(max_length=10)
class ownerAdmin(admin.ModelAdmin):
    list_display=["Model","Car_no","Quality","Year_prod","Colour"]
```


## OUTPUT
![alt text](<screenshot 1.jpg>)


## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
