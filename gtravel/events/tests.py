"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase
from events.models import Event



class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class EventTest(TestCase):
    def setUp(self):
        self.guade_2014 = Recipe(
            Event,
            event_name='GUADEC 2014',
            applications_start_date=datetime.date(4, 1, 2014),
            applications_deadline=datetime.date(5, 1, 2014),
            start_date=datetime.date(7, 26, 2014),
            end_date=datetime.date(8, 1, 2014),
            description=\
                "GUADEC 2014 will be taking place in Strasbourg, France."
                " This lovely city in walking distance from Germany was "
                "ranked the third most innovative city in France, and is"
                " home to several large tech companies and startups.",
            budget=20000,
            event_type=Event.LARGE_EVENT_GUADEC
        )
        self.guade_2015 = Recipe(
            Event,
            event_name='GUADEC 2015',
            applications_start_date=datetime.date(4, 1, 2015),
            applications_deadline=datetime.date(5, 1, 2015),
            start_date=datetime.date(7, 26, 2015),
            end_date=datetime.date(8, 1, 2015),
            description=\
                "GUADEC is the main conference for GNOME users, developers,"
                "foundation leaders, individuals, governments and businesses"
                " worldwide. GUADEC is not just a software conference though!"
                "People come together to meet collaborators from chat rooms "
                "and mailing lists, to network, to visit old friends and make"
                " new ones, and to have fun. In 2015, GUADEC will happen in "
                "Gothenburg, Sweden. See you there!",
            budget=20000,
            event_type=Event.LARGE_EVENT_GUADEC
        )


