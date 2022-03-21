from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group
from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    groups = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','gender', 'groups')


class CustomUserChnageForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'gender', 'groups')