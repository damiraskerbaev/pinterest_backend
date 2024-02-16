from django.db.models import *

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    fullname = CharField(
        'Fullname of the user',
        max_length=256
    )

    profil_picture=ImageField(
        'Picture of the profile',
        upload_to='profile-images/'
    )


    def __str__(self):
        return f'{self.username}'

    class Meta:
        verbose_name='User'
        verbose_name_plural='Users'