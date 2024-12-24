from django.db.models import Count, Sum, F
from django.http import JsonResponse
from Santa_list.models import SantasList, Kid
from Toy_factory.models import Toy

def statistics(request):
    if request.method == "GET":
        lists_data = []
        for santas_list in SantasList.objects.all():
            lists_data.append({
                "list_name": santas_list.name,
                "nice_kids_count": len(santas_list.nice_list),
                "naughty_kids_count": len(santas_list.naughty_list)
            })

        return JsonResponse({"lists": lists_data}, safe=False)
    return JsonResponse({"error": "Method not allowed"}, status=405)

def statistics_toys(request):
    if request.method == "GET":
        toy_counts = (
            Kid.objects.filter(niceness_coefficient__gte=6).values('gift__name')
            .annotate(
                required_quantity=Count('gift'),
                total_production_time=Sum(F('gift__production_time'))
            )
        )

        toys_data = [
            {
                "name": toy['gift__name'],
                "required_quantity": toy['required_quantity'],
                "total_production_time": toy['total_production_time']
            }
            for toy in toy_counts
        ]

        overall_production_time = sum(toy['total_production_time'] for toy in toy_counts)

        overall_toy_count = sum(toy['required_quantity'] for toy in toy_counts)

        total_houses = Kid.objects.count()
        total_delivery_time = total_houses * 1.5  # 1.5 hours per house

        return JsonResponse(
            {
                "toys_needed": toys_data,
                "overall_production_time": overall_production_time,
                "overall_toy_count": overall_toy_count,
                "total_delivery_time": total_delivery_time,
                "total_needed_time": total_delivery_time + overall_production_time
            },
            safe=False,
        )

    return JsonResponse({"error": "Method not allowed"}, status=405)