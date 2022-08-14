from django.urls import path, include
from . import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', MyloginView.as_view(),name='login'),
    path('news/', views.news, name='news'),
    path('logout/', LogoutView.as_view(next_page='/'),name='logout')
]