from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    username = None  # Remove username field
    name = models.CharField(max_length=150, blank=False, verbose_name=_("Full Name"))
    email = models.EmailField(unique=True, verbose_name=_("Email Address"))
    password = models.CharField(max_length=128, verbose_name=_("Password"))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def save(self, *args, **kwargs):
        # Ensure password is hashed before saving
        if not self.password.startswith("pbkdf2_"):  # Avoid re-hashing
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)