from django import forms
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    cnab_file = forms.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['txt'])
    ],
    label=''
    )