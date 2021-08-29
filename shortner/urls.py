from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name="home"),
    path('/generate-url', views.createUrl, name="generate-url"),
    path('<str:pk>', views.browse, name="browse"),
]
