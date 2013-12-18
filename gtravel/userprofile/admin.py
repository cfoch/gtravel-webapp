from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User


from userprofile.models import Persona

"""
class ProfileAdmin(UserAdmin):
    date_hierarchy = 'date_joined'
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
"""

admin.site.register(Persona)
