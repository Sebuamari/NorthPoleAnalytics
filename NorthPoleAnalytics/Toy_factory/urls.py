from django.urls import path
from .views import toy_factory, produce_toys

urlpatterns = [
    path('', toy_factory, name="toy_factory"),
    path('produce/', produce_toys, name="produce_toys"),
]