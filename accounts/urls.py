from django.urls import path

from accounts.views import registerPage, loginPage, logoutPage

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
]
