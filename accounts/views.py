from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView
from django.contrib.auth.models import User
from django.contrib import auth
from posts.models import NewPost

class SignUp(View):


    def post(self, request, *args, **kwargs):
        chars = set('~`!@#$%^&*():;\[]}{,.<>?')
        if request.POST['password1'] == request.POST['password2']:
            if any((c in chars) for c in request.POST['username']):
                return render(request, 'accounts/signup.html', {'error':'Username must be without special chars'})
            else:
                if len(request.POST['password1']) < 6:
                    return render(request, 'accounts/signup.html', {'error':'Password must match'})
                else:
                    try:
                        user = User.objects.get(username=request.POST['username'])
                        return render(request, 'accounts/signup.html', {'error':'Username has already been taken'})
                    except User.DoesNotExist:
                        user = User.objects.create_user(request.POST['username'], request.POST['email'], password=request.POST['password1'])
                        auth.login(request,user)
                        return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error':'Password must match'})

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/signup.html')

class LogIn(View):

    def post(self, request, *args, **kwargs):
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error' : 'username or password is incorrect.'})

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html')

class LogOut(View):

    def post(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('home')

class Profile(ListView):
    template_name = 'accounts/profile.html'
    model = NewPost
    context_object_name = 'all_announces_by_user'

    def get_queryset(self):
        return NewPost.objects.filter(user=self.request.user)


