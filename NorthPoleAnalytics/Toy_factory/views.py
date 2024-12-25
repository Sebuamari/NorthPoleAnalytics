from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Toy, Coal
from Santa_list.models import Kid
from helpers import are_you_santa

@login_required(login_url='/login/')
def toy_factory(request):
    are_you_santa(request)

    if request.method == "GET":
        toys_data = {
            "toys": [
                {
                    "name": toy.name,
                    "toy_type": toy.toy_type,
                    "quantity": toy.quantity
                } for toy in Toy.objects.all()
            ],
            "coals": [
                {
                    "quantity": coal.quantity
                } for coal in Coal.objects.all()
            ]
        }
        return JsonResponse(toys_data, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@login_required(login_url='/login/')
def toy(request, id):
    are_you_santa(request)

    if request.method == "GET":
        try:
            toy = Toy.objects.get(id=id)

            toy_data = {
                "name": toy.name,
                "toy_type": toy.toy_type,
                "quantity": toy.quantity
            }

            return JsonResponse(toy_data, safe=False)
        except Toy.DoesNotExist:
            return JsonResponse({'error': 'Toy not found'}, status=404)

    return JsonResponse({"error": "Method not allowed"}, status=405)

@login_required(login_url='/login/')
@csrf_exempt
def produce_toys(request):
    are_you_santa(request)

    if request.method == "POST":
        toy_requirements = (
            Kid.objects.filter(niceness_coefficient__gte=6)
            .values('gift__id')
            .annotate(required_quantity=Count('gift'))
        )
        response = {
            "toys_produced": [],
            "coal_produced": [],
        }

        for requirement in toy_requirements:
            toy_id = requirement['gift__id']
            required_quantity = requirement['required_quantity']

            toy = Toy.objects.filter(id=toy_id).first()
            if toy:
                if toy.quantity < required_quantity:
                    additional_quantity_needed = required_quantity - toy.quantity
                    Toy.objects.filter(id=toy_id).update(quantity=F('quantity') + additional_quantity_needed)
                    response["toys_produced"].append({
                        "name": toy.name,
                        "produced_quantity": additional_quantity_needed
                    })

        naughty_kids_count = Kid.objects.filter(niceness_coefficient__lt=6).count()

        coal = Coal.objects.first()
        if coal:
            if coal.quantity < naughty_kids_count:
                additional_coal_needed = naughty_kids_count - coal.quantity
                Coal.objects.update(quantity=F('quantity') + additional_coal_needed)
                response["coal_produced"] = {
                    "name": coal.name,
                    "produced_quantity": additional_coal_needed
                }

        if response["toys_produced"] or response["coal_produced"]:
            return JsonResponse(response)
        else:
            return JsonResponse({"message": "No production needed! Santa's ready to go!"})
    return JsonResponse({"error": "Method not allowed"}, status=405)

@login_required(login_url='/login/')
@csrf_exempt
def generate_gifts(request):
    are_you_santa(request)

    if request.method == "GET":
        kids = Kid.objects.all()
        response = {
            "generated_gifts": []
        }

        for kid in kids:
            if kid.niceness_coefficient > 6:
                response["generated_gifts"].append({
                    kid.name: kid.gift.name
                })
            response["generated_gifts"].append({
                kid.name: "Coal"
            })
        return JsonResponse(response)
    return JsonResponse({"error": "Method not allowed"}, status=405)