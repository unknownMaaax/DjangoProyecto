from django import forms
from django.forms import fields, models
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from tours.models import Usuario
from django.views import generic

class SignUpForm(UserCreationForm):
    rut = forms.CharField(max_length=10, required=True, help_text='')

    class Meta:
        model = Usuario
        fields = ('username','rut','password1','password2', )

class SignUp(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# Create your views here.
