from django.db import models
from users.models import CustomUser  # Import the CustomUser model

class Admin(CustomUser):
    """
    Admin model that inherits from CustomUser and adds a title.
    """
    title = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.title} - {self.email}" if self.title else self.email
