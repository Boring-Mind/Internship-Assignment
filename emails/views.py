from django.views.generic import TemplateView


class SuccessEmailView(TemplateView):
    template_name = 'success.html'
