from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import redirect, get_object_or_404, render
from ..models import Vehicles


@login_required
@permission_required('sell.delete_vehicle', raise_exception=True)
def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicles, id=id)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('filter_list')
    template_name = 'sell/vehicle_delete.html'
    context = {'vehicle': vehicle}
    return render(request, template_name, context)
