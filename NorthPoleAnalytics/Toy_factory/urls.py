from django.urls import path
from .views import toy_factory, produce_toys, toy, generate_gifts

urlpatterns = [
    path('', toy_factory, name="toy_factory"),
    path('<int:id>/', toy, name='toy'),
    path('produce/', produce_toys, name="produce_toys"),
    path('generate/', generate_gifts, name="generate_gifts"),
]