from django.views.generic import CreateView
from .models import Member

class UserCreateView(CreateView):
    model = Member
    template_name =  'gestor/login.html'
    fields = ('username', 'password')