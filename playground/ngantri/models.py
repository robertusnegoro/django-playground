from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    comingdate = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True)
