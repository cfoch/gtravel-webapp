from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    STATUS = (
        (0, 'pending'),
        (1, 'sponsorship offered'),
        (2, 'awaiting receipts'),
        (3, 'payment instructed'),
        (4, 'payment sent'),
        (5, 'completed'),
    )

    MEMBERSHIP_STATUS = (
        (0, 'Yes'),
        (1, 'Pending'),
        (2, 'Emeritus'),
        (3, 'No'),
    )

    id_user = models.ForeignKey(User)
    #id_event = models.Foreignkey(Event)
    employment = models.CharField(max_length=50, null=True)
    membership_status = models.IntegerField(max_length=1, choices=MEMBERSHIP_STATUS)
    date_of_arrival = models.DateField()
    date_of_departure = models.DateField()
    statement_of_interest = models.TextField()
    years_using_gnome = models.IntegerField()
    travel_costs = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    travel_costs_description = models.TextField()
    lodging_costs = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    lodging_costs_description = models.TextField()
    other_costs = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    other_costs_description = models.TextField()
    requested_subsidy_total = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    reimbursement_amount = models.DecimalField(default=0, max_digits=8, decimal_places=2, null=True)
    status = models.IntegerField(max_length=1, choices=STATUS, null=True)

class GnomeProjects(models.Model):
    gnome_project = models.CharField(max_length=50)


class ProjectsPerApplication(models.Model):
    id_application = models.ForeignKey(Application)
    id_gnome_project = models.ForeignKey(GnomeProjects)
    other_gnome_project = models.CharField(max_length=50, null=True)


class RolesPerApplication(models.Model):
    ROLES = (
        (0, 'Participant'),
        (1, 'Speaker'),
        (2, 'Organizer'),
        (3, 'Other'),
    )
    id_application = models.ForeignKey(Application)
    role = models.IntegerField(max_length=1, choices=ROLES)
    other_role = models.CharField(max_length=50, null=True)


class Receipts(models.Model):
    id_application = models.ForeignKey(Application)
    receipt = models.FileField(upload_to="receipts/%Y/%M")


class Reimbursement(models.Model):
    REIMBURSEMENT_TYPE = (
        (0, 'Check'),
        (1, 'Paypal'),
        (2, 'Bank transfer'),
        (3, 'Cash'),
    )
    
    #Or should everything go in this class? (BankTrasnfer, Check and Paypal)
    id_application = models.ForeignKey(Application)
    reimbursement_type = models.IntegerField(max_length=1, choices=REIMBURSEMENT_TYPE)


class BankTransfer(models.Model):
    id_reimbursement = models.OneToOneField(Reimbursement)
    holder_firstname = models.CharField(max_length=50)
    holder_lastname = models.CharField(max_length=50)
    holder_address = models.CharField(max_length=100)
    iban = models.CharField(max_length=30, null=True)
    account = models.CharField(max_length=30, null=True)
    swift = models.CharField(max_length=30, null=True)
    bic = models.CharField(max_length=30, null=True)
    bank_name = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=200)
    currency = models.CharField(max_length=3)


class PayPal(models.Model):
    id_reimbursement = models.OneToOneField(Reimbursement)
    account = models.EmailField()
    currency = models.CharField(max_length=3)

class Check(models.Model):
    id_reimbursement = models.OneToOneField(Reimbursement)
    account = models.CharField(max_length=30)
    address = models.CharField(max_length=100)    