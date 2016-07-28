from django.contrib.auth.models import User
from django import forms

from .models import UserProfile, Pet


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserProfileForm(forms.ModelForm):
    STATE_OPTS = [
        ('New York', 'NY'),
        ('Massachusetts', 'MA'),
        ('California', 'CA'),
    ]

    address1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATE_OPTS, widget=forms.Select(attrs={'class': 'form-control'}))
    zip_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = UserProfile
        fields = ('address1', 'address2', 'city', 'state', 'zip_code')


class PetForm(forms.ModelForm):
    PET_TYPE_OPTS = [
        ('dog', 'Dog'),
    ]
    SEX_OPTS = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    pet_type = forms.ChoiceField(choices=PET_TYPE_OPTS, widget=forms.Select(attrs={'class': 'form-control'}))
    breed = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex= forms.ChoiceField(choices=SEX_OPTS, widget=forms.RadioSelect())
    age = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Pet
        fields = ('name', 'pet_type', 'breed', 'sex', 'age', 'weight')
