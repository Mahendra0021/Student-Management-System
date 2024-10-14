from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = (
        (1, 'HDD'),
        (2, 'STAFF'),
        (3, 'STUDENT'),  # Ensure unique values for each user type
    )

    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField(upload_to='profile_pic/', blank=True, null=True)

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # on_delete options like CASCADE or SET_NULL are important
