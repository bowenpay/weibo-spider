from django.contrib import admin
from .models import Config, Friend, Weibo, Word


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'kind', 'value')
    list_filter = ['kind']


class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'screen_name', 'description')


class WeiboAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')


class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'kind', 'text')
    list_filter = ['kind']


admin.site.register(Config, ConfigAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Weibo, WeiboAdmin)
admin.site.register(Word, WordAdmin)