from django.urls import path, re_path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('device_data/', views.device_data, name='device_data'),
    path('login/', views.login_view, name="login"),
    path('register/', views.register, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('global/', views.global_view, name="global"),
    path('addDevice/', views.add_device, name="addDevice"),
    re_path(r'^.*\.html', views.pages, name='pages'),
]