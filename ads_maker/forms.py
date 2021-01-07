from django import forms
from django.core.exceptions import ValidationError
import logging


from .models import WSite
import string
logger = logging.getLogger('kromm_info')


class NewSiteForm(forms.Form):
    def clean_url(self):
        have_point = False
        cleaned_data = self.cleaned_data['url'].lower()
        accepted = string.ascii_lowercase + '.:/-' + string.digits
        # TODO: it must be a regex
        for letter in cleaned_data:
            have_point = have_point or letter == '.'
            if letter not in accepted:
                logger.warning(f'Wrong symbols {letter} in {cleaned_data}')
                raise ValidationError('It is not an URL')
        if not have_point:
            logger.warning(f'No point in {cleaned_data}')
            raise ValidationError('It is not an URL')
        if not cleaned_data.startswith('http://')\
                and not cleaned_data.startswith('https://'):
            cleaned_data = 'http://' + cleaned_data
        return cleaned_data

    url = forms.CharField(
        max_length=50,
        min_length=5,
        label='Site URL',
        help_text='Enter your homepage address',
        # required=True,
        # error_messages={'required': 'Please enter your name'},
        # validators=[url_validator(),],
        required=True,
    )
