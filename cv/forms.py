from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.Form):
    def clean_phone(self):
        pattern = R'^\+*\d{7,12}'
        phone = self.cleaned_data.get('phone')
        if not re.match(pattern, phone):
            raise ValidationError(_('Введите телефон от 7 до 12 цифр, может начинаться с +'))
        return phone

    first_name = forms.CharField(
        label=_('Имя'),
        max_length=100,
        required=True,
    )
    last_name = forms.CharField(
        label=_('Фамилия'),
        max_length=100,
        required=True,
    )
    email = forms.EmailField(label='Email', required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'you@example.com'}))
    phone = forms.CharField(label=_('Телефон'), required=False, max_length=15,
                            widget=forms.TextInput(attrs={'placeholder': '+493031234567'}))
    address = forms.CharField(label=_('Почтовый адрес'), required=False, max_length=250,
                              widget=forms.TextInput(attrs={'placeholder': 'Pariser Platz 1, 10000 Berlin'}))
    message = forms.CharField(label=_('Сообщение'), required=False,
        widget=forms.Textarea(attrs={'rows': '4'}))
