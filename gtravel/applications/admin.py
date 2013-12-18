from django.contrib import admin
from applications.models import Application, GnomeProject, Role

admin.site.register(Application)
admin.site.register(GnomeProject)
admin.site.register(Role)
