from django.urls import path
from .views import toy_factory

urlpatterns = [
    path('', toy_factory, name="toy_factory"),
]