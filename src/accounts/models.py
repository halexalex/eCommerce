from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):  # Custom user class
    email     = models.EmailField(max_length=255, unique=True)
    # full_name = models.CharField(max_length=255, blank=True, null=True)
    active    = models.BooleanField(default=True)
    staff     = models.BooleanField(default=False)
    admin     = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    # confirm   = models.BooleanField(default=False)
    # confirmed_date = models.DateTimeField()

    USERNAME_FIELD = 'email'  # username
    # email and password are required by default
    REQUIRED_FIELDS = []  # ["full_name"] # python manage.py createsuperuser

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     extend extra data


class GuestEmail(models.Model):
    email     = models.EmailField()
    active    = models.BooleanField(default=True)
    update    = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
