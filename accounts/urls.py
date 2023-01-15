from django.urls import path

from accounts.views import registerPage, loginPage, logoutPage, channelPage, become_content_creator, subscribe, likes

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('channel/<slug:username>/likes', likes, name='likes'),
    path('channel/<slug:username>/subscribe', subscribe, name='subscribe'),
    path('channel/<slug:username>/become_content_creator', become_content_creator, name='become_content_creator'),
    path('channel/<slug:username>/', channelPage, name='channel'),
]
