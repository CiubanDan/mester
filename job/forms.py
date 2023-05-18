from django import forms

from job.models import Job
from member.models import Category


class JobCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.CharField(disabled=True, initial='Open')

    class Meta:
        model = Job
        fields = ['title', 'job_description', 'location', 'price', 'status', 'contact_number']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a title'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add the location'}),
            'job_description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Add the description of the job'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'suffix': 'RON'}),
            'contact_number': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Insert your contact Number'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].label = 'Price (RON)'