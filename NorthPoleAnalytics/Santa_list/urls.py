from django.urls import path
from .views import santas_list, santas_list_naughty, santas_list_nice, kid

urlpatterns = [
    path('', santas_list, name="santas_list"),
    path('<int:id>/', kid, name='kid'),
    path('naughty/', santas_list_naughty, name="santas_list_naughty"),
    path('nice/', santas_list_nice, name="santas_list_nice"),
]