import datetime
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.contrib.auth.models import Group
from django.forms.extras.widgets import SelectDateWidget
from django.forms.widgets import TextInput
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from models import *
#cfrom captcha.fields import CaptchaField

class StudentForm(ModelForm):
#    data_Nascimento = forms.DateField(blank=True, null= False, required = True, widget= SelectDateWidget)
    class Meta:
        model = Student
        fields = studentFieldsList
        required = studentFieldsList
        widgets = {'data_Nascimento' : forms.DateInput(attrs={'type':'date'}), 'DRE': TextInput,
                   'RG': TextInput, 'rg_validade' : forms.DateInput(attrs={'type':'date'}),'passaporte_numero' : TextInput,
                   'CEP': TextInput , 'telefone': TextInput ,
                   'passaporte_validade' : forms.DateInput(attrs={'type':'date'}),
                   'numero_agencia' : TextInput, 'numero_conta' : TextInput
                  }

class StudentUpdateForm(StudentForm):
    class Meta:
        model = Student
        fields = studentFieldsList
        required = studentFieldsList
        widgets = {'data_Nascimento' : forms.DateInput(attrs={'type':'date'}), 'DRE': TextInput,
                   'RG': TextInput, 'rg_validade' : forms.DateInput(attrs={'type':'date'}),'passaporte_numero' : TextInput,
                   'CEP': TextInput , 'telefone': TextInput ,
                   'passaporte_validade' : forms.DateInput(attrs={'type':'date'}),
                   'numero_agencia' : TextInput, 'numero_conta' : TextInput
                  }

#        exclude = ('user',)
class OrientadorForm(ModelForm):
    class Meta:
        model = Orientador
        fields = orientadorFieldsList
        required = orientadorFieldsList
        widgets = {'data_Nascimento' : forms.DateInput(attrs={'type':'date'}),
                   'contato': TextInput,'numero_Registro': TextInput,
                   'CPF': TextInput
                  }

class OrientadorUpdateForm(OrientadorForm):
    class Meta:
        model = Orientador
        fields = orientadorFieldsList
        required = orientadorFieldsList
        widgets = {'data_Nascimento' : forms.DateInput(attrs={'type':'date'}),
                   'contato': TextInput,'numero_Registro': TextInput,
                   'CPF': TextInput
                  }
        
        exclude = ('user',)

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/test-lps2/home/")
    else:
        form = UserCreationForm()
    return render(request, "registration/register2.html", {
        'form': form,
    })
