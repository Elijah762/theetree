from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.views.generic.edit import FormView
from .forms import FileFieldForm


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def ProfileView(request):
    return render(request, 'account-manager/profile.html')


class UpdateFileView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'
    success_url = 'profile'


def post(self, request, *args, **kwargs):
    form_class = self.get_form_class()
    form = self.get_form(form_class)
    files = request.FILES.getlist('file_field')
    if form.is_valid():
        for f in files:
            ...  # Do something with each file.
        return self.form_valid(form)
    else:
        return self.form_invalid(form)
