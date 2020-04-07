from django import forms
from .models import User

class LoginForm(forms.Form):
    username=forms.CharField(
        label='账户名称',
        min_length=4,
        max_length=16,
        error_messages={'min_length': '最小长度4位','max_length': '最大长度16位'},
        widget=forms.TextInput(),
    )

    password=forms.CharField(
        label='账户密码',
        min_length=4,
        max_length=16,
        error_messages={'min_length': '最小长度4位', 'max_length': '最大长度16位'},
        widget=forms.PasswordInput(),
    )

    class Meta:
        models=User
        fields=['username','password']