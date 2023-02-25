from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import UserRegistration
# Create your views here.

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    template_name = 'accounts/profile.html'
    context = {
        'session': 'profile',
    }
    return render(request, template_name, context )


def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistration(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        user_form = UserRegistration()
    return render(request, 'accounts/registration.html', {'user_form': user_form})