from django.core import mail
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from users.models import User

from .forms import EmailForm


class SuccessEmailView(TemplateView):
    template_name = 'success.html'


class EmailFormView(FormView):
    template_name = 'index.html'
    form_class = EmailForm
    success_url = reverse_lazy('success')

    def send_email(self, form):
        subject = form.cleaned_data['subject']
        sender = self.request.user.email
        message = form.cleaned_data['message']
        receivers = User.objects.only("email").values()
        receivers = [r['email'] for r in receivers if bool(r['email'])]

        if not bool(receivers):
            # If receivers list is empty
            return
        
        email = mail.EmailMessage(subject, message, sender, receivers)
        email.send()

    def form_valid(self, form):
        self.send_email(form)
        return super().form_valid(form)
