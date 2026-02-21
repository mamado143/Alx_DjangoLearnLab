from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,
        null=True,
        default='profile_pictures/default.jpg'
    )

    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username

    def follower_count(self):
        return self.followers.count()

    def following_count(self):
        return self.following.count()
