from django import forms
from .models import Job

class OfferForm(forms.Form):
    title   = forms.CharField(label='Titulo',max_length=256)
    url     = forms.URLField(label='URL',max_length=512)
    body    = forms.CharField(label='Mensaje', widget=forms.Textarea)

    def save(self):
        data = self.cleaned_data
        job = Job()
        job.title   = data['title']
        job.url     = data['url']
        job.body    = data['body']
        return job.save()
