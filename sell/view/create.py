from django.shortcuts import render, redirect
from ..forms import VehicleForm
from django.contrib.auth.decorators import permission_required, login_required


@login_required
@permission_required('sell.create_vehicle', raise_exception=True)
def vehicle_create(request):
    template_name = 'sell/vehicle_create.html'
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('filter_list')
    else:
        form = VehicleForm()
    context = {'form': form}
    return render(request, template_name, context)