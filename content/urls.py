from django.urls import path

from content.views import upload, video, like, dislike, create_playlist

urlpatterns = [
    path('upload/', upload, name='upload'),
    path('video/<int:id>/like', like, name='like'),
    path('video/<int:id>/dislike', dislike, name='dislike'),
    path('video/<int:id>/create_playlist', create_playlist, name='create_playlist'),
    path('video/<int:id>', video, name='video'),
]
