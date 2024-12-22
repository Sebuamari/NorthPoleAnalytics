from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Kid, SantasList

@csrf_exempt
def santas_list(request):
    if request.method == "GET":
        kids_data = serialize_kids(Kid.objects.all())
        return JsonResponse(kids_data, safe=False)

    elif request.method == "POST":
        name = request.POST.get('name')
        niceness_coefficient = request.POST.get('niceness_coefficient')
        gift = request.POST.get('gift')
        santas_list_id = request.POST.get('santas_list')

        if not all([name, niceness_coefficient, gift, santas_list_id]):
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        try:
            santas_list = SantasList.objects.get(id=santas_list_id)
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

@csrf_exempt
def kid(request, id):
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

def santas_list_naughty(request):
    if request.method == "GET":
        santa_list = SantasList.objects.first()
        naughty_kids = santa_list.naughty_list
        kids_data = serialize_kids(naughty_kids)
        return JsonResponse(kids_data, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def santas_list_nice(request):
    if request.method == "GET":
        santa_list = SantasList.objects.first()
        nice_kids = santa_list.nice_list
        kids_data = serialize_kids(nice_kids)
        return JsonResponse(kids_data, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def serialize_kids(kids):
    return {
        "kids": [
            {
                "name": kid.name,
                "gift": kid.gift,
                "niceness_coefficient": kid.niceness_coefficient,
                "santas_list": {
                    "name": kid.santas_list.name
                } if kid.santas_list else None
            } for kid in kids
        ]
    }