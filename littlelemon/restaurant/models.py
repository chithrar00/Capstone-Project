from django.db import models

class Menu(models.Model):
    ID = models.IntegerField(max_length=5,primary_key=True),
    Title=models.CharField(max_length=255),
    Price=models.DecimalField(10,2),
    Inventory=models.IntegerField(max_length=5),
    def __str__(self): 
        return self.first_name
class Booking(models.Model):
    ID = models.IntegerField(max_length=11,primary_key=True),
    Name = models.CharField(max_length=255),
    No_of_guests = models.IntegerField(max_length=6),
    BookingDate=models.DateTimeField(),
    def __str__(self): 
        return self.first_name
# Create your models here.
