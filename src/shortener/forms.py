from django import forms
from .validators import validate_url, validate_dot_com

class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        label="",
        validators=[validate_url],
        widget=forms.TextInput(
                attrs={
                    "placeholder" : "Long url to shorten",
                    "class": "form-control",
                }
        ))

    #whenever form.is_valid() is called, clean is called.

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm,self).clean()
    #     url = cleaned_data.get('url')
    #     return url

    #clean_<fieldName> will be called whenever there is form.is_valid() is called.
    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     urlvalidator = URLValidator()
    #     try:
    #         urlvalidator(url)
    #     except:
    #         raise forms.ValidationError("Invalid URL.")
    #     return url

