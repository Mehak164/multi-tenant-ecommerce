from django.db import models

# Create your models here.
from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name
