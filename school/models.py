from django.db import models

class School(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'school'  # Explicitly set table name

    def __str__(self):
        return self.school_name

