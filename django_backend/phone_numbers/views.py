from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse

from phone_numbers.models import Range


def index(request):
    return render(request, 'index.html')


def search(request):
    number = request.GET.get('number')
    range = Range.get_by_number(number)
    return render(
        request, 'index.html', 
        {'number': number, 'operator': range.operator, 'region': range.region}
    )


def search_json(request):
    number = request.GET.get('number')
    range = Range.get_by_number(number)
    return JsonResponse(model_to_dict(range))
