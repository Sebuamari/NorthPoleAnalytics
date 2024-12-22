from django.http import JsonResponse
from .models import Toy

def toy_factory(request):
    if request.method == "GET":
        toys_data = {
            "toys": [
                {
                    "name": toy.name,
                    "toy_type": toy.toy_type,
                    "quantity": toy.quantity
                } for toy in Toy.objects.all()
            ]
        }
        return JsonResponse(toys_data, safe=False)
