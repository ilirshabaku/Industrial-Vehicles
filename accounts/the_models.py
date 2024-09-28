from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)  # Auto-incrementing field
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return self.full_name
