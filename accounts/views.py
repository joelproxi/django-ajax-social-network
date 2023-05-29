from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from accounts.forms import UserRegistration
from apps.models import Post


# Create your views here.

@login_required
def profile(request: HttpRequest) -> HttpResponse:
    template_name: str = 'accounts/profile.html'
    post_list = Post.objects.all()
    context = {
        'session': 'profile',
        'post_list': post_list,
    }
    return render(request, template_name, context)


@login_required
def user_list(request: HttpRequest) -> HttpResponse:
    template_name: str = 'user/list.html'
    user_list = User.objects.all()
    context = {
        'session': 'user',
        'user_list': user_list,
    }
    return render(request, template_name, context)
    

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