from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    # path('<str:name>/', views.greeting, name="greeting"),
    path('isItChristmas/', views.is_it_christmas, name="isItChristmas"),
]