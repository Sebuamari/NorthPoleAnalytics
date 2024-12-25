from django.http import JsonResponse

def are_you_santa(request):
    if request.user.username != "santa":
        return JsonResponse({"error": "Stop being naughty! You're not santa."}, status=403)