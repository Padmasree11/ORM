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


