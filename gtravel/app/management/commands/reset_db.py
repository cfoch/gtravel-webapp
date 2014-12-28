import datetime
from model_mommy.recipe import Recipe

from django.db import connection
from django.core.management.base import BaseCommand, CommandError

from events.models import Event
from userprofile.models import Persona

class Command(BaseCommand):
    # args = '<poll_id poll_id ...>'
    # help = 'Closes the specified poll for voting'
    def __reset_db(self):
        print("Drop tables")
        cursor = connection.cursor()
        cursor.execute('show tables;')
        parts = ('DROP TABLE IF EXISTS %s;' % table for (table,) in cursor.fetchall())
        sql = 'SET FOREIGN_KEY_CHECKS = 0;\n' + '\n'.join(parts) + 'SET FOREIGN_KEY_CHECKS = 1;\n'
        connection.cursor().execute(sql)
        print("All tables has been droped")

    def _create_users(self):
        admin = Persona(username='gtravel')
        admin.set_password('gtravel')
        admin.save()


    def _create_events(self):
        print("Populating events")
        guadec_2014 = Recipe(
            Event,
            event_name='GUADEC 2014',
            applications_start_date=datetime.date(2014, 4, 1),
            applications_deadline=datetime.date(2014, 5, 1),
            start_date=datetime.date(2014, 7, 26),
            end_date=datetime.date(2014, 8, 1),
            description=\
                "GUADEC 2014 will be taking place in Strasbourg, France."
                " This lovely city in walking distance from Germany was "
                "ranked the third most innovative city in France, and is"
                " home to several large tech companies and startups.",
            budget=20000,
            event_type=Event.LARGE_EVENT_GUADEC
        )
        guadec_2014.make()
        guadec_2015 = Recipe(
            Event,
            event_name='GUADEC 2015',
            applications_start_date=datetime.date(2015, 4, 1),
            applications_deadline=datetime.date(2015, 5, 1),
            start_date=datetime.date(2015, 7, 26),
            end_date=datetime.date(2015, 8, 1),
            description=\
                "GUADEC is the main conference for GNOME users, developers,"
                "foundation leaders, individuals, governments and businesses"
                " worldwide. GUADEC is not just a software conference though!"
                "People come together to meet collaborators from chat rooms "
                "and mailing lists, to network, to visit old friends and make"
                " new ones, and to have fun. In 2015, GUADEC will happen in "
                "Gothenburg, Sweden. See you there!",
            budget=28000,
            event_type=Event.LARGE_EVENT_GUADEC
        )
        guadec_2015.make()

    def handle(self, *args, **options):
        self.__reset_db()
        self._create_users()
        self._create_events()
