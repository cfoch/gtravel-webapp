import datetime
"""
import random

from model_mommy.recipe import Recipe
from events.models import Event
"""
def is_applicant(user):
    return user.groups.filter(name='applicant').count() == 1
"""
def event_recipe(event_name, description, event_type, year=None):
    random_timestamp = random.uniform(0, time.time())
    start_date = datime.date.from_timestamp(random_timestamp)
    if year is not None:
      start_date.replace(year=year)
    return Recipe(
        Event,
        event_name=event_name,
        applications_start_date=start_date - datetime.timedelta(months=3)
        applications_deadline=start_date - datetime.timedelta(months=1),
        start_date=start_date,
        end_date=start_date + datetime.timedelta(days=10),
        description=description,
        budget=random.randint(50000, 100000),
        event_type=event_type
    )
"""
