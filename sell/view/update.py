from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, redirect, get_object_or_404
from ..forms import VehicleForm
from ..models import Vehicles


@login_required
@permission_required('sell.update_vehicle', raise_exception=True)
def update_vehicle(request, id):
    template_name = 'sell/vehicle_update.html'
    item = get_object_or_404(Vehicles, id=id)

    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('filter_list')
    else:
        form = VehicleForm(instance=item)

    context = {'form': form}
    return render(request, template_name, context)
