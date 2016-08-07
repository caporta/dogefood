from django.http import HttpResponse, JsonResponse
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


@login_required(login_url='login/')
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
            resp_data = {}
            form.save()

            resp_data['name'] = pet.name
            resp_data['pet_type'] = pet.pet_type
            resp_data['breed'] = pet.breed
            resp_data['sex'] = pet.sex
            resp_data['age'] = pet.age
            resp_data['weight'] = pet.weight

            return JsonResponse(resp_data)

        # html = render_to_string(template_name, {'form': form, 'petpk': pk}, context_instance=RequestContext(request))
        # return HttpResponse(html)







