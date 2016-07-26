from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.shortcuts import render, render_to_response

from .forms import UserForm, UserProfileForm

def register(request):
    context = RequestContext(request)
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
            print('user_form.errors, profile_form.errors')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('registration/new_user.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)



