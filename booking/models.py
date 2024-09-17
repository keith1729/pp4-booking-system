from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Booking(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  email = models.EmailField()
  date = models.DateField()
  time = models.TimeField()
  number_of_players = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return f"Booking by {self.user.username} on {self.date} at {self.time} for {self.number_of_players} players!"


