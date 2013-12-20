from django.contrib import admin
from applications.models import Application, GnomeProject, Role, Check, BankTransfer

admin.site.register(Application)
admin.site.register(GnomeProject)
admin.site.register(Role)
admin.site.register(Check)
admin.site.register(BankTransfer)
