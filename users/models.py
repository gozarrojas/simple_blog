from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # OneToOneField - Relación de uno a uno y PROTECT evitamos eliminar el usuario
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    website = models.URLField(max_length=200, blank=True)
    photo = models.ImageField(upload_to='users/pictures', blank=True, null=True)
    data_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
