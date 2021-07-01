from django import forms
from genero.models import Genero
class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        #Quais campos você quer
        fields = '__all__'