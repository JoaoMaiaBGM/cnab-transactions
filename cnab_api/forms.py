from django import forms
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='', 
        validators=[
            FileExtensionValidator(allowed_extensions=["txt"])
        ],
    )