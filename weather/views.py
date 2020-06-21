from django.http import JsonResponse

# Create your views here.


def meteohome(request, city):
    data = {
        'text': "Vous avez demandé la météo de " + city
    }
    return JsonResponse(data)
