from django import forms
from .models import UserInfo
class UserInfoForm(forms.ModelForm):
    class Meta:
        model=UserInfo
        fields="__all__"
        widgets={
            "u":forms.HiddenInput(),
            'sh':forms.HiddenInput(),
            'company':forms.TextInput(attrs={'class':'realname'}),
            'position':forms.TextInput(attrs={'class':'realname'}),
            'hobby':forms.TextInput(attrs={'class':'hobby'}),
            'reason':forms.TextInput(attrs={'class':'hobby'}),
            "realname":forms.TextInput(attrs={'class':'realname'})
        }


