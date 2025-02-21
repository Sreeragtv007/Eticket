from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customuser(models.Model):

    ROLE = (
        ('Admin', 'admin'),
        ('User', 'user'),
        ('Organizer', 'organizer')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE)

    def __str__(self):
        return self.user.username
