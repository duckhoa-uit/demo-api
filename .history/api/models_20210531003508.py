from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male', null=True, blank=True)
    avatar = models.ImageField(default="default-avatar.png", null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    following = models.ManyToManyField('self', blank=True, symmetrical=False, related_name="followers")
    link_facebook = models.URLField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.email}'

    @register.filter()
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "date_joined": self.date_joined.strftime("%b %d %Y, %I:%M %p"),
            "avatar_url": self.avatar.url,
        }
    def is_valid_birthday(self):
        return self.birthday > timezone.now()