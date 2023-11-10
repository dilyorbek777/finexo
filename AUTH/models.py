from django.contrib.auth.models import User
from django.db import models

class Dashboard(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='user/', null=True, blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.user.username