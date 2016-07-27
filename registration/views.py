from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from .forms import UserForm, UserProfileForm, PetForm

def register_user(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # commit=False allows us to delay saving until manually setting user attr
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True

            user = authenticate(username=user_form.cleaned_data['username'],
                                password=user_form.cleaned_data['password'],
                                )
            login(request, user)
        else:
            print(user_form.errors)
            print(profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render('registration/new_user.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def register_pet(request):
    registered = False

    if request.method == 'POST':
        pet_form = PetForm(data=request.POST)

        if pet_form.is_valid():
            # commit=False allows us to delay saving until manually setting user attr
            pet = pet_form.save(commit=False)
            pet.owner = request.user
            pet.save()

            registered = True

            return HttpResponseRedirect(reverse('home'))

        else:
            print(pet_form.errors)
    else:
        pet_form = PetForm()

    return render('registration/new_pet.html', {'pet_form': pet_form, 'registered': registered})
