from django.shortcuts import render
from ..models import Vehicles

# Create your views here.

def vehicles_shop(request):
    template_name = 'sell/shop.html'
    vehicle_list = Vehicles.objects.all()
    context = {'vehicle_list': vehicle_list}
    return render(request, template_name, context)