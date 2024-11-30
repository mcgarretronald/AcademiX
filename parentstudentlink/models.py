from django.db import models
from parent.models import Parent
from  student.models  import Student
# Create your models here.
class ParentStudentLink(models.Model):
    id = models.AutoField(primary_key=True)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=50)  # E.g., Father, Mother, Guardian
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.parent} -> {self.student} ({self.relationship})"
