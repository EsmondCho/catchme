from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_freshmen', 'catching_count')


admin.site.register(Profile, ProfileAdmin)