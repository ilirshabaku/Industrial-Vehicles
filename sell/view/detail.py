from django.shortcuts import render, get_object_or_404
from ..models import Vehicles


def detail(request, id):
    template_name = 'sell/detail.html'
    info = get_object_or_404(Vehicles, id=id)
    context = {'info': info}
    return render(request, template_name, context)