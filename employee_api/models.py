from django.db import models
import uuid


class Employee(models.Model):
    employee_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    middle_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=255, default="")
    birth_date = models.DateField(db_index=True)
    admission_date = models.DateField(db_index=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
