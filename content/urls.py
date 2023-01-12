from django.urls import path

from content.views import upload, video

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('video/<int:id>', video, name='video'),
]
