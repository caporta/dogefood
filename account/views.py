from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='login/')
def home(request):
    pets = request.user.pet_set.all()
    return render(request, 'home.html', {'pets': pets})


def pet_update(request, pk, template_name=''):
    pass
