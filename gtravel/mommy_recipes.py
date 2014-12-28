from model_mommy.recipe import Recipe
from events.models import Event

event = Recipe(
  Event,
  event_name='GUADEC 2014',
  applications_start_date=,
  applications_deadline=,
  start_date=,
  end_date=,
  description='GUADEC 2014 will take place in Strasbourg, France, on 26 July-1 August. These pages are related to organising the event. If you want to attend or sponsor the conference, please visit http://2014.guadec.org.',
  budget=60000,
  event_type=Event.LARGE_EVENT_GUADEC
)
