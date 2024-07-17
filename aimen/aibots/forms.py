from django import forms

from .models import AibotOrder


class AibotOrderForm(forms.ModelForm):
    class Meta:
        model = AibotOrder
        fields = ('title', 'requirements',)

