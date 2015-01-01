import datetime
from model_mommy.recipe import Recipe

from django.db import connection
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from django.contrib.auth.models import Group

from events.models import Event
from userprofile.models import Persona
from applications.models import GnomeProject, Role

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
        print("All tables has been dropped")

    def _create_groups(self):
        print("Populating Groups")
        group_names = [
            'admin',
            'board',
            'travel committee',
            'administrative assistant',
            'applicant'
        ]
        for group_name in group_names:
            group = Recipe(Group, name=group_name)
            group.make()
        print("Groups has been created")

    def _create_users(self):
        print("Populating users")
        default_password = "pass"

        admin_user = Persona.objects.create_superuser(
            username='gtravel-admin',
            email=None,
            password='gtravel-admin')
        admin_group = Group.objects.get(name='admin')
        admin_user.groups.add(admin_group)
        admin_user.save()

        board_user = Persona.objects.create_superuser(
            username='board-user',
            email=None,
            password=default_password)
        board_group = Group.objects.get(name='board')
        board_user.groups.add(board_group)
        board_user.save()

        travel_committee_user = Persona.objects.create_superuser(
            username='travel-committee-user',
            email=None,
            password=default_password)
        travel_committee_group = Group.objects.get(name='travel committee')
        travel_committee_user.groups.add(travel_committee_group)
        travel_committee_user.save()

        administrative_assistant_user = Persona.objects.create_superuser(
            username='administrative-assistant-user',
            email=None,
            password=default_password)
        administrative_assistant_group = Group.objects.get(
            name='administrative assistant')
        administrative_assistant_user.groups.add(administrative_assistant_group)
        administrative_assistant_user.save()

        applicant_user = Persona.objects.create_superuser(
            username='applicant-user',
            email=None,
            password=default_password)
        applicant_group = Group.objects.get(name='applicant')
        applicant_user.groups.add(applicant_group)
        applicant_user.save()

        print("Users has been created")

    def _create_roles(self):
        print("Populating Roles")
        role_names = [
            'Participant',
            'Speaker',
            'Organizer'
        ]
        for role_name in role_names:
            role = Recipe(Role, role=role_name, is_default=True)
            role.make()
        print("Roles has been created")

    def _create_gnome_projects(self):
        print("Populating GNOME Projects")
        project_names = [
            'pitivi',
            'gstreamer',
            'evince',
            'gnome-music',
            'gnome-web',
            'gnome-terminal'
        ]
        for project_name in project_names:
            project = Recipe(GnomeProject, gnome_project=project_name)
            project.make()
        print("GNOME Projects has been created")

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
        print("Events has been created")

    def handle(self, *args, **options):
        self.__reset_db()
        call_command('syncdb', interactive=False)
        self._create_groups()
        self._create_users()
        self._create_roles()
        self._create_gnome_projects()
        self._create_events()
