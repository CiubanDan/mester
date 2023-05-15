from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import  TextInput, EmailInput

from member.models import CustomMember


class CustomMemberForm(UserCreationForm):
    member_type = ((False, 'Member'), (True, "Worker"))
    is_worker = forms.ChoiceField(choices=member_type, widget=forms.Select(attrs={'class': "form-control"}))

    class Meta:
        model = CustomMember
        fields = ['first_name', 'last_name', 'email', 'phone_number']
        widgets = {
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your First Name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Last Name'}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your EMAIL'}),
            'phone_number': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your PhoneNumber'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter your password'}),
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please re-enter your password'})

    def clean(self):
        """
        This function checks if there is already someone registered with email
        """

        cleaned_data = self.cleaned_data
        get_email = cleaned_data['email']
        check_emails = CustomMember.objects.filter(email=get_email)
        if check_emails:
            msg = "This email is already used please enter another email"
            self._errors['email'] = self.error_class([msg])

        return cleaned_data


class AuthenticationNewForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', "placeholder": 'Enter your Email'}
        )
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control', "placeholder": 'Enter your Password'}
        )
