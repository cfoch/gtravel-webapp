from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Persona(AbstractBaseUser):
    #FIXME: Is there a better field for phone numbers?
    #Check: https://github.com/stefanfoulis/django-phonenumber-field
    phone_number = models.CharField(
        verbose_name="Phone number",
        max_length=15,
        null=True
    )
    #blog = models.URLField()
    facebook = models.URLField(
        verbose_name="Facebook Profile",
        null=True
    )
    website = models.URLField(
        verbose_name="Website or blog",
        null=True
    )
    twitter = models.URLField(
        verbose_name="Twitter Profile",
        null=True
    )
    """
    linkedin = models.URLField(
        verbose_name="Linkedin",
        null=True
    )
    """
    googleplus = models.URLField(
        verbose_name="Google+ Profile",
        null=True
    )
