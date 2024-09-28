from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from ..models import Vehicles


# Create your views here.
@login_required
@permission_required('sell.vehicle_list', raise_exception=True)
def vehicles_list(request):
    template_name = 'sell/filter_list.html'
    vehicle_list = Vehicles.objects.all()
    context = {'vehicle_list': vehicle_list}
    return render(request, template_name, context)