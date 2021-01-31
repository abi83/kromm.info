from django import forms
from django.core.exceptions import ValidationError
import logging
import re


# from ads_maker.models import WSite
import string
logger = logging.getLogger('kromm_info')


class NewSiteForm(forms.Form):
    def clean_url(self):
        """

        """
        homepage_url_pattern = R'^(https?:\/\/)?(www)?\.?(\w+\.)+\w+\/?$'
        web_url_pattern = R'^(https?:\/\/)?(www)?\.?(\w+|\-\.)+\w+\/?'
        cleaned_data = self.cleaned_data['url'].lower()
        url_match = re.match(web_url_pattern, cleaned_data)
        homepage_match = re.match(homepage_url_pattern, cleaned_data)
        if not url_match:
            logger.warning(f'No match to url in {cleaned_data}')
            raise ValidationError('It is not an URL')
        if not homepage_match:
            logger.warning(f'Not a homepage: {cleaned_data}')
            raise ValidationError('It is not a Homepage')
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
