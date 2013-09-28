from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    ROLE_CHOICES = (
        (0, 'Participant'),
        (1, 'Speaker'),
        (2, 'Organizer'),
        (3, 'Other'),
    )

    STATUS_CHOICES = (
        (0, 'pending'),
        (1, 'sponsorship offered'),
        (2, 'awaiting receipts'),
        (3, 'payment instructed'),
        (4, 'payment sent'),
        (5, 'completed'),
    )

    id_user = models.Foreignkey(User)
    role = models.IntegerField(max_length=1, choices=ROLE_CHOICES)
    other_role = models.CharField(max_length=50, null=True)
    date_of_arrival = models.DateField()
    date_of_departure = models.DateField()
    statement_of_interest = models.TextField()
    employment = models.CharField(max_length=50, null=True)
    status = models.IntegerField(max_length=1, choices=STATUS_CHOICES)
    years_using_gnome = models.IntegerField()
