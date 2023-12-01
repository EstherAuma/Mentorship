from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    occupation = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"