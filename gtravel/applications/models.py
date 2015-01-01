from django.db import models
from django_iban.fields import IBANField, SWIFTBICField

from events.models import Event
from userprofile.models import Persona


class GnomeProject(models.Model):
    gnome_project = models.CharField(max_length=50)

    def __unicode__(self):
        return self.gnome_project

class Role(models.Model):
    role = models.CharField(max_length=30)
    is_default = models.BooleanField()

    def __unicode__(self):
        return self.role

class Application(models.Model):
    STATUS = (
        (0, 'pending'),
        (1, 'sponsorship offered'),
        (2, 'awaiting receipts'),
        (3, 'payment instructed'),
        (4, 'payment sent'),
        (5, 'completed'),
        (6, 'withdrawn'),
    )

    (MEMBERSHIP_STATUS_YES,
    MEMBERSHIP_STATUS_PENDING,
    MEMBERSHIP_STATUS_EMERITUS,
    MEMBERSHIP_STATUS_NO) = range(4)

    MEMBERSHIP_STATUS = (
        (0, 'Yes'),
        (1, 'Pending'),
        (2, 'Emeritus'),
        (3, 'No'),
    )

    REIMBURSEMENT_TYPE = (
        (0, 'Check'),
        (1, 'Paypal'),
        (2, 'Bank transfer'),
        (3, 'Cash'),
    )

    user = models.ForeignKey(Persona)
    employment = models.CharField(
        verbose_name="Employement",
        max_length=50,
        null=True
    )
    gnome_projects = models.ManyToManyField(
        GnomeProject,
        verbose_name="GNOME Project",
        null=True
    )
    membership_status = models.IntegerField(
        verbose_name="Membership status",
        max_length=1,
        choices=MEMBERSHIP_STATUS
    )
    event = models.ForeignKey(Event)
    roles = models.ManyToManyField(
        Role,
        limit_choices_to={'is_default': True}
    )
    date_of_arrival = models.DateField(
        verbose_name="Date of arrival"
    )
    date_of_departure = models.DateField(
        verbose_name="Date of departure"        
    )
    statement_of_interest = models.TextField(
        verbose_name="Statement of interest"
    )
    years_using_gnome = models.IntegerField(
        verbose_name="Number of years using GNOME",
        max_length=2
    )
    travel_costs = models.DecimalField(
        verbose_name="Travel costs",
        default=0,
        max_digits=8,
        decimal_places=2
    )
    travel_costs_description = models.TextField(
        verbose_name="Travel costs description"
    )
    lodging_costs = models.DecimalField(
        verbose_name="Lodging costs",
        default=0,
        max_digits=8,
        decimal_places=2
    )
    lodging_costs_description = models.TextField(
        verbose_name="Lodging costs",
    )
    other_costs = models.DecimalField(
        verbose_name="Other costs",
        default=0,
        max_digits=8,
        decimal_places=2
    )
    other_costs_description = models.TextField(
        verbose_name="Other costs description"
    )
    requested_subsidy_total = models.DecimalField(
        verbose_name="Requested subsidy total",
        help_text="This is the amount you would like covered by" \
            "the GNOME Foundation",
        default=0,
        max_digits=8,
        decimal_places=2
    )
    reimbursement_amount = models.DecimalField(
        verbose_name="Reimbursement amount",
        default=0,
        max_digits=8,
        decimal_places=2,
        null=True
    )
    status = models.IntegerField(
        verbose_name="Application status",
        max_length=1,
        choices=STATUS,
        null=True
    )
    reimbursement_type = models.IntegerField(
        verbose_name="Reimbursement type",
        max_length=1,
        choices=REIMBURSEMENT_TYPE
    )

    class Meta:
        unique_together = (("user", "event"), )
    
    def __unicode__(self):
        return "Application" + str(self.id)

class Negotiation(models.Model):
    answer_to = models.OneToOneField(
        'self',
        related_name='+',
        null=True
    )
    id_application = models.ForeignKey(Application)
    group = models.ForeignKey('auth.Group')
    approved = models.NullBooleanField()
    reason = models.TextField()
    amount = models.DecimalField(
        default=0,
        max_digits=8,
        decimal_places=2
    )
    date = models.DateField()

class ProjectsPerApplication(models.Model):
    application = models.ForeignKey(Application)
    gnome_project = models.ForeignKey(GnomeProject)
    other_gnome_project = models.CharField(
        max_length=50,
        null=True
    )
"""
class RolesPerApplication(models.Model):
    ROLES = (
        (0, 'Participant'),
        (1, 'Speaker'),
        (2, 'Organizer'),
        (3, 'Other'),
    )
    application = models.ForeignKey(Application)
    role = models.IntegerField(
        max_length=1,
        choices=ROLES
    )
    other_role = models.CharField(
        max_length=50,
        null=True
    )
"""

class Receipts(models.Model):
    application = models.ForeignKey(Application)
    receipt = models.FileField(upload_to="receipts/%Y/%M")

class BankTransfer(models.Model):
    application = models.OneToOneField(Application, related_name='+')
    holder_firstname = models.CharField(max_length=50)
    holder_lastname = models.CharField(max_length=50)
    holder_address = models.CharField(max_length=100)
    iban = IBANField(null=True)
    account = models.CharField(
        max_length=30,
        null=True
    )
    swift_bic = SWIFTBICField(null=True)
    bank_name = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=200)
    currency = models.CharField(max_length=3)


class PayPal(models.Model):
    application = models.OneToOneField(Application, related_name='+')
    account = models.EmailField()
    currency = models.CharField(max_length=3)

class Check(models.Model):
    application = models.OneToOneField(Application, related_name='+')
    account = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    
