from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Fligths(models.Model):
    flight_company=models.CharField()
    flight_name=models.CharField()
    flight_number=models.IntegerField()
    From=models.CharField()
    to=models.CharField()
    departure_time=models.TimeField()
    flight_date=models.DateField()
    ticket_price=models.IntegerField()

class user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    flight = models.ForeignKey(Fligths, on_delete=models.PROTECT)

    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    adhar = models.CharField(max_length=12)
    phno = models.CharField(max_length=10)

    seat_class = models.CharField(max_length=20)
    seat_number = models.IntegerField()


"""
WHY WE HAVE TO USE ONETOONEFIELD MEANS ONE AUTH USE SHOULD HAVE ONLY ONE RECORED
BECAUSE WHEN WE ACCESS THROUGH SESSION THEN IT BECOME DIFFICULT BECAUSE

IF WE USE ONLY FOREIGN KEY MEANS IF REQUEST.USER.EXTRAINFO ITS TAKES MULTIPLE RECORDS SO NEEDED LOOP TO ACCESS
IF ONETONE MEANS ONLY ONE RECORED RECORD SO  NO NEED LOOP TO ACESSS


"""

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    flight=models.ForeignKey(Fligths,on_delete=models.PROTECT)
    name=models.CharField()
    email=models.EmailField()
    age=models.IntegerField()
    adhar=models.IntegerField()
    phno=models.IntegerField()
    seat_class=models.CharField()
    seat_number=models.IntegerField()



