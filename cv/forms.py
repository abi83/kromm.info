from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
import re


class ContactForm(forms.Form):
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_return = ''
        for letter in phone:
            if letter in '0123456789':
                phone_return += letter
        if 7 <= len(phone_return) <= 12:
            return phone_return
        else:
            raise ValidationError(_('В телефоне должно быть от 7 до 12 цифр'))


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
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        min_length=5,
        help_text=_('Введите корректный е-мейл'),
        widget=forms.TextInput(
            attrs={'placeholder': 'you@example.com', 'type': 'email'}
        )
    )
    phone = forms.CharField(
        label=_('Телефон'),
        required=False,
        max_length=25,
        min_length=5,
        help_text=_('От 7 до 25 знаков. Допускаются цифры, скобки (), пробелы и знаки + и -. Можно оставить пустым.'),
        widget=forms.TextInput(
            attrs={'placeholder': '+49 (303) 123-4567',
                   'type': 'tel',
                   'pattern': '[0-9\-\(\)\+\s]{7,}',}
        )
    )
    address = forms.CharField(
        label=_('Почтовый адрес'),
        required=False,
        max_length=250,
        widget=forms.TextInput(
            attrs={'placeholder': 'Pariser Platz 1, 10000 Berlin'}))
    message = forms.CharField(
        label=_('Сообщение'),
        required=False,
        widget=forms.Textarea(attrs={'rows': '4'}))
