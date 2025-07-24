from django.contrib import admin
from .models import Bookings,Bookingseats
# Register your models here.
@admin.register(Bookings)
class BookingsAdmin(admin.ModelAdmin):
    list_display = ['id','user','showtime','booking_time','total_amount','booking_status']

@admin.register(Bookingseats)
class Bookingseats(admin.ModelAdmin):
    list_display = ['booking','seat'] 