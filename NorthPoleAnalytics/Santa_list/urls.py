from django.urls import path
from .views import santa_list

urlpatterns = [
    path('', santa_list, name="santa_list"),
]