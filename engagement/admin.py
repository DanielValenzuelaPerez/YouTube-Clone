from django.contrib import admin

from engagement.models import Subscription, ContentEngagement, ContentComment

admin.site.register(Subscription)
admin.site.register(ContentEngagement)
admin.site.register(ContentComment)
