from django.contrib import admin

from accounts.models import Creator


class CreatorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']


admin.site.register(Creator, CreatorAdmin)
