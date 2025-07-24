from django.db import models
from accounts.models import User
from movies.models import Movies

# Create your models here.
class Theatre(models.Model):
    name=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=2000)
    manager=models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)  


    def __str__(self):
        return self.name


class Showtimes(models.Model): 
    movie = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True, blank=True)
    theater = models.ForeignKey(Theatre, on_delete=models.CASCADE) 
    show_time = models.DateTimeField()
    screen_number = models.BigIntegerField(null=True, blank=True) 

class Seats(models.Model):
    theater = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    screen_number = models.IntegerField(null=True,blank=True)
    row_label = models.CharField(max_length=10)
    seat_number = models.IntegerField()
    seat_type = models.CharField(max_length=20, choices=[['gold','Gold'],['silver','Silver']])

