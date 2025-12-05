from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from tenants.models import Tenant

class User(AbstractUser):
    ROLE_CHOICES = (
        ('owner', 'Owner'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')

    def __str__(self):
        return f"{self.username} ({self.role})"
