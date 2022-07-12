from distutils.command.upload import upload
from django import forms
from .models import New

# Enlazar el modelo para generarlo automáticamente
# Modelo de formulario
class NewForm(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'description', 'author', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Título'}),
            'description': forms.Textarea(attrs={'class':'form-control',}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Autor'}),
        }
        labels = {
            'title':'', 'description':'', 'author':'', 'image':''
        }