from django import forms
from .models import *





class ConsultasForm(forms.Form):
    cnombre = forms.CharField(label="Nombre",max_length=20,required=True)
    capellido = forms.CharField(label="Apellido",max_length=20,required=True)
    cemail = forms.EmailField(label="Email", required=True)
    cconsulta = forms.CharField(label="Consulta",required=True,widget=forms.Textarea(attrs={"rows":"","cols":""}))

