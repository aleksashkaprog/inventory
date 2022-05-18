from django import forms
from inventory_bd.models import Responsible, Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = '__all__'


class ResponsibleForm(forms.ModelForm):
    class Meta:
        model = Responsible
        fields = '__all__'



