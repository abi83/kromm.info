from django import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError




class ContactForm(forms.Form):
    def clean_phone(self):
        # TODO: make a phone validation via regex
        phone = self.cleaned_data.get('phone')
        for simbol in phone:
            if simbol not in '0123456789+':
                raise ValidationError('It is not a phone')
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
