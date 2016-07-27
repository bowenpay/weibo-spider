from django.contrib import admin
from .models import Config, Friend, Weibo


class ConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'kind', 'value')
    list_filter = ['kind']


class FriendAdmin(admin.ModelAdmin):
    list_display = ('id', 'screen_name', 'description')


class WeiboAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'created_at')

admin.site.register(Config, ConfigAdmin)
admin.site.register(Friend, FriendAdmin)
admin.site.register(Weibo, WeiboAdmin)