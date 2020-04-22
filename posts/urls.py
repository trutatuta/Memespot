from django.urls import path

from . import views

urlpatterns = [
    #path('', views.HomePage.as_view(), name='home'),
    path('create/', views.Add.as_view(), name='create'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('<int:pk>/edit/', views.Update.as_view(), name='edit'),
    path('<int:pk>/delete/', views.Delete.as_view(), name='delete'),
    path('<int:pk>/up', views.UPostDetail.as_view(), name='detail_up'),
] 