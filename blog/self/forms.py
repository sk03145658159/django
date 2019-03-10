from userauth.models import User
from django import forms
from .models import Article
class Articleform(forms.ModelForm):
    class Meta:
        model=Article
        fields=['k','c','title','con','status']
        widgets={
            # 'a':forms.HiddenInput(),
            'c':forms.Select(attrs={
                'class':'ckt'
            }),
            'k':forms.Select(attrs={
                'class':'ckt'
            }),
            'title':forms.TextInput(attrs={
                'class':'ckt'
            }),
            'con':forms.TextInput(),
            'status':forms.CheckboxInput()

        }
    # def clean(self):  # 钩子函数首先执行
    #     cleaned_data = super().clean()
