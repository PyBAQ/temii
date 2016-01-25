# forms.py
from django import forms
from .models import Charla


class PostularCharlaForm(forms.ModelForm):
	class Meta:
		model = Charla
		exclude = ['fecha_taller', 'estado', 'votos', 'usuario']