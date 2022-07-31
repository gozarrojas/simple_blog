from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from users.forms import SignupForm


# Una vista que muestra un formulario. En caso de error,
# vuelve a mostrar el formulario con errores de validación;
# en caso de éxito, redirige a una nueva URL.
class SignupView(FormView):
    template_name = 'users/register.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:registerok')


class LoginView(auth_views.LoginView):
    template_name = 'users/login.html'
