from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View, generic
from django.views.generic import UpdateView, CreateView

from inventory_bd.models import Thing, Responsible, General
import sqlite3
from inventory_bd.forms import ThingForm, ResponsibleForm


class MainView(View):
    def get(self, request):
        return render(request, 'inventory_bd/main.html')


def bd_list(request, *args, **kwargs):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("""select id, name, code, inv, price, count, summ, note, resp_id from inventory_bd_thing""")
    tables = cursor.fetchall()
    my_id = conn.cursor()
    my_id.execute("""select id from inventory_bd_thing""")
    qr = conn.cursor()
    qr.execute("""select id from inventory_bd_thing""")
    return render(request, 'inventory_bd/thing_table.html', {'tables': tables, 'my_id': my_id, 'qr': qr})


class QRView(View):
    def get(self, request, profile_id):
        thing = Thing.objects.get(id=profile_id)
        inventory_form = ThingForm(instance=thing)
        return render(request, 'inventory_bd/qrcode.html',
                      context={'inventory_form': inventory_form, 'profile_id': profile_id})

    def post(self, request, profile_id):
        thing = Thing.objects.get(id=profile_id)
        inventory_form = ThingForm(request.POST, instance=thing)

        return render(request, 'inventory_bd/qrcode.html',
                      context={'inventory_form': inventory_form, 'profile_id': profile_id})



class ThingCreateView(CreateView):
    model = Thing
    fields = ['name', 'code', 'inv', 'price', 'count', 'summ', 'note', 'resp']

    def form_valid(self, form):
        Thing.objects.create(**form.cleaned_data)

        return HttpResponseRedirect(reverse('thing-list'))


class ThingUpdateView(UpdateView):
    model = Thing
    template_name_suffix = '_update_form'
    fields = ['name', 'code', 'inv', 'price', 'count', 'summ', 'note', 'resp']

    def form_valid(self, form):
        form.save(commit=True)

        return HttpResponseRedirect(reverse('thing-list'))


class RespListView(generic.ListView):
    model = Responsible
    template_name = 'responsible_list.html'
    context_object_name = 'responsible_list'


def responsible_list(request, *args, **kwargs):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute("""select id, name from inventory_bd_responsible""")
    tables = cursor.fetchall()
    my_id = conn.cursor()
    my_id.execute("""select id from inventory_bd_responsible""")

    return render(request, 'inventory_bd/responsible_all.html', {'tables': tables, 'my_id': my_id})



class RespUpdateView(UpdateView):
    model = Responsible
    template_name_suffix = '_update_form'
    fields = ['name']

    def form_valid(self, form):
        form.save(commit=True)

        return HttpResponseRedirect(reverse('resp-list'))

class RespCreateView(CreateView):
    model = Responsible
    fields = ['name']

    def form_valid(self, form):
        Responsible.objects.create()

        return HttpResponseRedirect(reverse('resp-list'))



class GeneralListView(generic.ListView):
    model = General
    template_name = 'general_list.html'
    context_object_name = 'general_list'


class GeneralUpdateView(UpdateView):
    model = General
    template_name_suffix = '_update_form'
    fields = ['people', 'product']

    def form_valid(self, form):
        form.save(commit=True)

        return HttpResponseRedirect(reverse('general-list'))

class GeneralCreateView(CreateView):
    model = General
    fields = ['people', 'product']

    def form_valid(self, form):
        Responsible.objects.create()

        return HttpResponseRedirect(reverse('general-list'))

