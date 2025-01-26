from django.db import models

# Create your models here.
SHIFTS = (
    ("1", "Morning"),
    ("2", "Afternoon"),
    ("3", "Evening"),
)

class Reservations(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    shift = models.CharField(max_length=1, choices=SHIFTS)  # Add the shift field
    number_phone = models.IntegerField()
    time_log = models.TimeField(help_text="(hour:min:sec)")

