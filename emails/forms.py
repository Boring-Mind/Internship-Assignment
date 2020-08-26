from crispy_forms import layout
from crispy_forms.helper import FormHelper
from django import forms
from django.urls import reverse


class EmailForm(forms.Form):
    subject = forms.CharField(
        max_length=120,
        required=False,
        help_text='120 characters max'
    )
    message = forms.CharField(
        max_length=1000,
        widget=forms.widgets.Textarea
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-EmailForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('index')
