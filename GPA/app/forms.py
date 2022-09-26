from dataclasses import fields
from tkinter import HIDDEN
from django import forms
from .models import Register


class RegisterForm(forms.ModelForm):
  password=forms.CharField(widget=forms.HiddenInput())
  confirm_password=forms.CharField(widget=forms.HiddenInput())
  class Meta:
    model=Register
    fields="__all__"
  
  def clean(self):
    cleaned_data = super(RegisterForm, self).clean()
    password = cleaned_data.get("password")
    confirm_password = cleaned_data.get("confirm_password")

    if password != confirm_password:
      raise forms.ValidationError(
                "password and confirm_password does not match"
            )

