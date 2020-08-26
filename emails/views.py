from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import EmailForm


class SuccessEmailView(TemplateView):
    template_name = 'success.html'


class EmailFormView(FormView):
    template_name = 'index.html'
    form_class = EmailForm
    success_url = reverse_lazy('success')
