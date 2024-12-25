from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Kid, SantasList
from Toy_factory.models import Toy
from helpers import are_you_santa, serialize_kids

@login_required(login_url='/login/')
@csrf_exempt
def santas_list(request):
    are_you_santa(request)

    if request.method == "GET":
        kids_data = serialize_kids(Kid.objects.all())
        return JsonResponse(kids_data, safe=False)

    elif request.method == "POST":
        name = request.POST.get('name')
        niceness_coefficient = request.POST.get('niceness_coefficient')
        gift_id = request.POST.get('gift_id')
        santas_list_id = request.POST.get('santas_list')

        if not all([name, niceness_coefficient, gift_id, santas_list_id]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        try:
            gift = Toy.objects.get(id=gift_id)
            santas_list = SantasList.objects.get(id=santas_list_id)
        except Toy.DoesNotExist:
            return JsonResponse({'error': 'Toy not found'}, status=404)
        except SantasList.DoesNotExist:
            return JsonResponse({'error': 'SantaList not found'}, status=404)

        try:
            Kid.objects.create(
                name=name,
                niceness_coefficient=int(niceness_coefficient),
                gift=gift,
                santas_list=santas_list
            )

            return JsonResponse({
                'message': 'Kid added successfully!'
            }, status=201)
        except ValueError as e:
            return JsonResponse({'error': f'Invalid data: {e}'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Server error: {e}'}, status=500)

    return JsonResponse({"error": "Method not allowed"}, status=405)

@login_required(login_url='/login/')
@csrf_exempt
def kid(request, id):
    are_you_santa(request)

    if request.method == "GET":
        try:
            kid = Kid.objects.get(id=id)

            kid_data = {
                'name': kid.name,
                'niceness_coefficient': kid.niceness_coefficient,
                'gift': kid.gift,
                'santas_list': {
                    'id': kid.santas_list.id,
                    'name': kid.santas_list.name
                } if kid.santas_list else None
            }

            return JsonResponse(kid_data, safe=False)
        except Kid.DoesNotExist:
            return JsonResponse({'error': 'Kid not found'}, status=404)

    elif request.method == "DELETE":
        try:
            kid = Kid.objects.get(id=id)
        except Kid.DoesNotExist:
            return JsonResponse({"error": "Kid not found"}, status=404)

        kid.delete()
        return JsonResponse({"message": "Kid deleted successfully!"})

    return JsonResponse({"error": "Method not allowed"}, status=405)

@login_required(login_url='/login/')
def santas_list_naughty(request):
    are_you_santa(request)

    if request.method == "GET":
        santa_list = SantasList.objects.first()
        naughty_kids = santa_list.naughty_list
        kids_data = serialize_kids(naughty_kids)
        return JsonResponse(kids_data, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)

@login_required(login_url='/login/')
def santas_list_nice(request):
    are_you_santa(request)

    if request.method == "GET":
        santa_list = SantasList.objects.first()
        nice_kids = santa_list.nice_list
        kids_data = serialize_kids(nice_kids)
        return JsonResponse(kids_data, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)