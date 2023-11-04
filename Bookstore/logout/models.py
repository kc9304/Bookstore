from django.db import models

# Create your models here.
class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=100, blank=False)
    email = models.EmailField()
    password = models.CharField(max_length=100, blank=False)
    def _str_(self):
        return self.username

class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    quant = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def str(self):
        return self.title