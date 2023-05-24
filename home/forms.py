from django import forms
from .models import VagaCasa
class AdicionarVagaForm(forms.ModelForm):
     class Meta:
          model = VagaCasa
          fields = '__all__'