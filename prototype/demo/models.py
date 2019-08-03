from django.db import models


# Create your models here.
class Listing(models.Model):
    isbn = models.IntegerField(blank=True, null=True)
    class_name = models.CharField(max_length=200, blank=True, null=True)
    book_name = models.CharField(max_length=200, blank=True, null=True)
    seller_name = models.CharField(max_length=200, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.isbn
