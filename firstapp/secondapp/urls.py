from django.urls import path

from . import views

urlpatterns = [
    path('0', views.secondAppindex, name= 'index'),
    path('1', views.secondAppfirstindex, name= 'firstindex'),
    path('2', views.secondAppsecondindex, name= 'secondindex'),
    path('3', views.secondAppthirdindex, name= 'thirdindex'),
    path('4', views.secondAppfourthindex, name= 'fourthindex'),
]