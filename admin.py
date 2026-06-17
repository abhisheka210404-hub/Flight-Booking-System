from django.contrib import admin
from .models import Fligths

# Register your models here.

class FligthsAdmin(admin.ModelAdmin):
    list_display=['flight_company','flight_name','flight_number','From','to','departure_time','flight_date','ticket_price']
    list_display_link=['flight_name']

admin.site.register(Fligths,FligthsAdmin)
