from django import forms
from django.core.validators import FileExtensionValidator


class UploadFileForm(forms.Form):
    file = forms.FileField(
        label='',
        validators=[
            FileExtensionValidator(allowed_extensions=["txt"])
        ],
    )


class StoreFilter(forms.Form):
    store = forms.CharField(widget=forms.HiddenInput(), required=False)
