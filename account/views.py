from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from registration.models import Pet
from registration.forms import PetForm


@login_required(login_url='login/')
def home(request):
    pets = request.user.pet_set.all()
    return render(request, 'home.html', {'pets': pets})


def pet_form(request, pk):
    template_name = 'pet_form.html'
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == 'GET':
        form = PetForm(instance=pet)
        html = render_to_string(template_name, {'form': form, 'petpk': pk}, context_instance=RequestContext(request))
        return HttpResponse(html)
    if request.method == 'POST':
        form = PetForm(request.POST or None, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('/')
        # html = render_to_string(template_name, {'form': form, 'petpk': pk}, context_instance=RequestContext(request))
        # return HttpResponse(html)







