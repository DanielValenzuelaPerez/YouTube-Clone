from django.contrib import admin
from django.urls import path
from youtube.views import home_view
from accounts.views import account_create_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('account/create/', account_create_view),
]
