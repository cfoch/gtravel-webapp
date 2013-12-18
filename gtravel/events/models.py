from django.db import models
from datetime import date

class Event(models.Model):
    EVENT_TYPE = (
        ('Small Event', (
            (1, 'Hackfest'),
            (2, 'Other'),
        )),
        ('Large Event', (
            (3, 'GUADEC'),
            (4, 'GNOME.ASIA'),
            (5, 'Other'),
        )),
    )

    event_name = models.CharField(max_length=80)
    applications_start_date = models.DateField()
    applications_deadline = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    #city = models.CharField(30)
    budget = models.DecimalField(max_digits=8, decimal_places=2)
    event_type = models.IntegerField(max_length=1, choices=EVENT_TYPE)

    def upcoming(self):
        return self.start_date > date.today()

    def __unicode__(self):
        items = {
            "id": self.id,
            "event_name": self.event_name
        }
        return "Event #%(id)d - %(event_name)s" % items

