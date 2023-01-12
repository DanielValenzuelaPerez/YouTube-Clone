from django.urls import path

from content.views import upload, video, like

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('video/<int:id>/like', like, name='like'),
    path('video/<int:id>', video, name='video'),
]
