from django import forms
from . import models


class AdminPermissionForm(forms.ModelForm):
    title=forms.CharField(
        widget=forms.TextInput(),

    )

    url=forms.CharField(

    )

    action=forms.ModelMultipleChoiceField(
        queryset=models.Action.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
        initial=models.Action.objects.filter(code='GET'),
    )

    menu=forms.ModelChoiceField(
        queryset=models.Menu.objects.all()
    )

    class Meta:
        model = models.Permission
        fields = ['title','url','action','menu']