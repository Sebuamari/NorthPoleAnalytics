from django.urls import path
from .views import statistics, statistics_toys

urlpatterns = [
    path('', statistics, name="statistics"),
    path('toys/', statistics_toys, name="statistics_toys"),
]