from django.contrib import admin
from django.urls import path, include
from youtube.views import home_view

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls')),
    path('content/', include('content.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]
