from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("registration/", views.registration, name='registration'),
    path("signin/", views.signin, name='signin'),
    path("signout/", views.signout, name='signout'),
]
