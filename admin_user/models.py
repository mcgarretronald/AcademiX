from django.db import models
from django.conf import settings

class Admin(models.Model):
    """
    Admin model linked to the User model for role-specific attributes.
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="admin_profile"
    )
    department = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - Admin"
