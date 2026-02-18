from django import forms

class UploadXlsxForm(forms.Form):
    arquivo = forms.FileField()
