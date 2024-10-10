from django.db import models

# Create your models here.

class Client(models.Model):

    client_name = models.CharField(max_length=30)
    created_at = models.CharField(max_length=100)
    created_by = models.CharField(max_length=30)
