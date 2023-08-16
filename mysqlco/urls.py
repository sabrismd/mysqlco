from django.urls import path
from mysqlapp import views

urlpatterns = [
    path('check_connection/', views.check_connection),
]
