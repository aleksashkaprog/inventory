from django.urls import path
from .views import ThingUpdateView, QRView, ThingCreateView, MainView, bd_list, RespListView, RespUpdateView, \
    RespCreateView, GeneralListView, GeneralCreateView, GeneralUpdateView, responsible_list

from . import views

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('invetory/things/', bd_list, name='thing-list'),
    path('inventory/create_thing/', ThingCreateView.as_view(), name='create-thing'),
    path('inventory/<int:pk>/edit_thing/', ThingUpdateView.as_view(), name='edit-thing'),
    path('inventory/<int:profile_id>/qrcode/', QRView.as_view(), name='qrcode'),
    path('invetory/responsibles/', RespListView.as_view(), name='resp-list'),
    path('inventory/<int:pk>/edit_responsible/', RespUpdateView.as_view(), name='edit-resp'),
    path('inventory/create_responsible/', RespCreateView.as_view(), name='create-resp'),
    path('invetory/general/', GeneralListView.as_view(), name='general-list'),
    path('inventory/create_general/', GeneralCreateView.as_view(), name='create-general'),
    path('inventory/<int:pk>/edit_general/', GeneralUpdateView.as_view(), name='edit-general'),
    path('invetory/responsibles_all/', responsible_list, name='resp-all'),
    ]