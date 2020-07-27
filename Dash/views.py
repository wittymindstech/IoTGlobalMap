# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm, AddDeviceForm
from django.template import loader
from django import template
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Device
from django.core.serializers import serialize

@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = "Username or Password Doesn't match"
        else:
            msg = 'Error validating the form'

    return render(request, "account/login.html", {"form": form, "msg": msg})

def register(request):
    msg = None
    success = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            msg = 'User is created.'
            success = True
            login(request, user)
            return HttpResponseRedirect('/login')
    else:
        form = SignUpForm()
    return render(request, 'account/register.html', {'form': form, "msg": msg,"success": success})

@login_required(login_url="/login/")
def pages(request):
    context = {}
    try:
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('error-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('error-500.html')
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def global_view(request):
    return render(request, "global.html")

def device_data(request):
    device = serialize("geojson", Device.objects.all())
    return HttpResponse(device, content_type='json')

@login_required(login_url="/login/")
def add_device(request):
    if request.method == 'POST':
        form = AddDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Device Added successfully.')
            return redirect('addDevice')
    else:
        form = AddDeviceForm()
    return render(request, 'addDevice.html', {'form': form})

