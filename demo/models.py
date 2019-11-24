from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime


class CustomUser(AbstractUser):
    # Can add additional fields here
    def __str__(self):
        return self.email


# Create your models here.
class Listing(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default="None")
    isbn = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=200, blank=True, null=True)
    book_name = models.CharField(max_length=200, blank=True, null=True)
    seller_name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    upload_date = models.DateTimeField(default=datetime.datetime.now(), blank=True, null=True)

    def __str__(self):
        return self.isbn


class SoldBook(models.Model):
    # clone Listing and add new fields
    isbn = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=200, blank=True, null=True)
    book_name = models.CharField(max_length=200, blank=True, null=True)
    seller_name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    # New Fields
    sold_price = models.IntegerField(blank=True, null=True)
    customer_feedback = models.CharField(max_length=1000, blank=True, null=True)

