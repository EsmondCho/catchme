from django import forms

from .models import Senior

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Senior
        fields = ('name', 'image', )