from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Client

class RegistrationForm(UserCreationForm):

    class Meta:
        model = Client
        fields = (
            'client_username',
            'client_name',
            'client_surname',
            'client_pet',
            'client_telephone',
            'client_email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        new_client = super(RegistrationForm, self).save(commit=False)
        new_client.client_username = self.cleaned_data['client_username']
        new_client.client_name = self.cleaned_data['client_name']
        new_client.client_email = self.cleaned_data['client_email']

        if commit:
            new_client.save()

        return new_client