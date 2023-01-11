from django.urls import path

from content.views import upload

urlpatterns = [
    path('upload/', upload, name='upload'),
]
