from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, View
from posts.models import NewPost
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(LoginRequiredMixin, ListView):
    login_url = 'login'
    redirect_field_name = 'redirect_to'
    template_name = 'home.html'
    model = NewPost
    context_object_name = 'posts' 
    
