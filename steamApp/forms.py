from django import forms
from django.forms import CheckboxSelectMultiple

from steamApp.models import Product, Publisher, Developer, SteamUser


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        exclude = ["id", "creatorUser"]

class PublisherForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        label="Products",
        queryset=Product.objects.none(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )

    class Meta:
        model = Publisher
        fields = ['name', 'products']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['products'].queryset = Product.objects.filter(creatorUser=user)



class DeveloperForm(forms.ModelForm):
    products = forms.ModelMultipleChoiceField(
        label="Products",
        queryset=Product.objects.none(),
        widget=CheckboxSelectMultiple(attrs={"class": "form-check-input"}),
    )

    class Meta:
        model = Developer
        fields = ['name', 'products']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['products'].queryset = Product.objects.filter(creatorUser=user)


class SteamUserForm(forms.ModelForm):
    class Meta:
        model = SteamUser
        fields = "__all__"
        exclude = ["id", "creatorUser"]
