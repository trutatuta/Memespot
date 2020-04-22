from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView, UpdateView, DeleteView
from .models import NewPost
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class Add(LoginRequiredMixin, View):

    login_url = 'login'
    redirect_field_name = 'redirect_to'
    def post(self, request, *args, **kwargs):
        if request.FILES['image'] and request.POST['caption']:
            post = NewPost()
            post.image = request.FILES['image']
            post.caption = request.POST['caption']
            
            post.pub_date = timezone.datetime.now()
            
            post.user = request.user
            post.save()
            return redirect('/')
        else:
            return render(request, 'posts/add_new.html',{'error':'All fields are required'})


    def get(self, request, *args, **kwargs):
        return render(request, 'posts/add_new.html')




class PostDetail(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(NewPost, pk=kwargs['pk'])
        data = {'post':post}
        return render(request, 'posts/detail.html', data)

class Update(UpdateView):
    model = NewPost
    fields = ['caption']
    template_name = 'posts/post_edit.html'


class Delete(DeleteView):
    model = NewPost
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('home')

class UPostDetail(View):
    def get(self, request, *args, **kwargs):
        post = get_object_or_404(NewPost, pk=kwargs['pk'])
        data = {'post':post}
        return render(request, 'posts/detail_up.html', data) 
    





