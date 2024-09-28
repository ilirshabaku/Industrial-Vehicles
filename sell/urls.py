from django.urls import path
from .view.create import vehicle_create
from .view.detail import detail
from .view.update import update_vehicle
from .view.delete import delete_vehicle
from .view.vehicle_shop import vehicles_shop
from .view.filter import vehicle_filter_shop, vehicle_filter_list

urlpatterns = [
    path('', vehicles_shop, name='vehicle_shop'),
    path('vehicle/detail/<uuid:id>/', detail, name='vehicle_detail'),
    path('create/new/', vehicle_create, name='create_vehicle'),
    path('vehicle/<uuid:id>/update/', update_vehicle, name='update_vehicle'),
    path('vehicle/<uuid:id>/delete/', delete_vehicle, name='delete_vehicle'),
    path('filter_shop', vehicle_filter_shop, name='filter_shop'),
    path('filter_list', vehicle_filter_list, name='filter_list'),

]
