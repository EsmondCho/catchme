from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_freshman', 'catching_count')


class CatchingAdmin(admin.ModelAdmin):
    list_display = ('image', 'comment', 'like_count', 'chatting_count', 'is_in_pocket', 'is_recognized', 'confidence', 'registered_time', 'modified_time', 'senior', 'profile')


class SeniorAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'student_id', 'like_count', 'caught_count', 'registered_time', 'modified_time')


class ChattingAdmin(admin.ModelAdmin):
    list_display = ('chat', 'profile', 'catching', 'registered_time', 'modified_time')


class LikeAdmin(admin.ModelAdmin):
    list_display = ('profile', 'catching', 'registered_time', 'modified_time')




admin.site.register(Profile, ProfileAdmin)
admin.site.register(Catching, CatchingAdmin)
admin.site.register(Senior, SeniorAdmin)
admin.site.register(Chatting, ChattingAdmin)
admin.site.register(Like, LikeAdmin)





