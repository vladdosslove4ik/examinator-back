from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    blocked = models.BooleanField(default=False) #Jak true to zablokowany i nie da się na niego zalogować
    email = models.EmailField(max_length = 254)
    nickname = models.CharField(max_length=30, primary_key=True) 
    imie = models.CharField(max_length=254)
    nazwisko = models.CharField(max_length=254)
    haslo = models.CharField(max_length=200)
    

class BusinessUser(User):
    startSubscriptionDate = models.DateField(default=datetime.date.today)
    creditCardNumber = models.CharField(max_length=30, default="1111")
    creditCardExpirationDate = models.CharField(max_length=10)
    creditCardCode = models.CharField(max_length=8, default="1111")


class Moderator(models.Model):
    email = models.EmailField(max_length = 254)
    nickname = models.CharField(max_length=30)
    imie = models.CharField(max_length=254)
    nazwisko = models.CharField(max_length=254)
    haslo = models.CharField(max_length=200)