from django.db.models import Q
from django.shortcuts import render
from ..models import Vehicles

def vehicle_filter_shop(request):
    qs = Vehicles.objects.all()
    word_contains_query = request.GET.get('word_contains')
    word_exact_query = request.GET.get('word_exact')
    comment_price_year_old_query = request.GET.get('comment_price_year_old')

    if word_contains_query:
        qs = qs.filter(vehicle__icontains=word_contains_query)

    if word_exact_query:
        qs = qs.filter(vehicle__iexact=word_exact_query)

    if comment_price_year_old_query:
        qs = qs.filter(
            Q(price__icontains=comment_price_year_old_query) |
            Q(produce_year__icontains=comment_price_year_old_query) |
            Q(new_old__icontains=comment_price_year_old_query) |
            Q(description__icontains=comment_price_year_old_query)
        ).distinct()

    template_name = 'sell/filter_shop.html'
    context = {'queryset': qs}
    return render(request, template_name, context)


def vehicle_filter_list(request):
    qs = Vehicles.objects.all()
    word_contains_query = request.GET.get('word_contains')
    word_exact_query = request.GET.get('word_exact')
    comment_price_year_old_query = request.GET.get('comment_price_year_old')

    if word_contains_query:
        qs = qs.filter(vehicle__icontains=word_contains_query)

    if word_exact_query:
        qs = qs.filter(vehicle__iexact=word_exact_query)

    if comment_price_year_old_query:
        qs = qs.filter(
            Q(price__icontains=comment_price_year_old_query) |
            Q(produce_year__icontains=comment_price_year_old_query) |
            Q(new_old__icontains=comment_price_year_old_query) |
            Q(description__icontains=comment_price_year_old_query)
        ).distinct()

    template_name = 'sell/filter_list.html'
    context = {'qs': qs}
    return render(request, template_name, context)
