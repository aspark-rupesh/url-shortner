from django import forms

from shortner.models import ShortUrl


class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['original_url']
        
       