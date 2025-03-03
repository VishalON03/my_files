from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",  # 🔧 Fix conflict
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",  # 🔧 Fix conflict
        blank=True
    )

    def __str__(self):
        return self.email
