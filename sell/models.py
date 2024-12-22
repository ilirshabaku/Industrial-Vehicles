import uuid
from django.db import models

# Create your models here.

class Vehicles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vehicle = models.CharField(max_length=50, null=True, blank=True)  # Example: title, name, etc.
    description = models.TextField(max_length=900, blank=True, null=True)
    produce_year = models.IntegerField()
    horsepower = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0.00)
    price = models.IntegerField()
    image = models.ImageField(upload_to='sell/images/', blank=True, null=True)
    new_CHOICES = [
        ('new', 'new'),
        ('old', 'old'),
    ]
    new_old = models.CharField( max_length=3, choices=new_CHOICES, default='new')

    time_created = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField(default=1)

    class Meta:
        permissions = [
            ("vehicle_detail", "You Can view Items"),
            ("create_vehicle", "You Can Create Items"),
            ("update_vehicle", "You Can edit Items"),
            ("delete_vehicle", "You Can delete Items"),
        ]


    def __str__(self):
        return f'{self.vehicle}'





