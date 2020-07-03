# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from .forms import LoginForm, SignUpForm
from django.template import loader
from django import template
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Device
from .serializer import DeviceSerializer

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

    return render(request, "login.html", {"form": form, "msg": msg})


def register(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created.'
            success = True

            return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()
    return render(request, "register.html", {"form": form, "msg": msg, "success": success})

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
    map_access_token = "pk.eyJ1IjoiMnlhZGF2cmFqbmVlc2giLCJhIjoiY2pya2MycXFqMGp3bzQ0cXcxOWpvMTJnaCJ9.qacSuG9YNHGkh6_KQ_R3Hg"
    return render(request, "global.html", {"map_access_token":map_access_token})


@api_view(['POST'])
@csrf_exempt
class add_device(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'addDevice.html'

    def get(self, request):
        device = get_object_or_404(Device, pk=id)
        serializer = DeviceSerializer(device)
        return Response({'serializer': serializer, 'profile': device})

    def post(self, request, pk):
        device = get_object_or_404(Device, pk=id)
        serializer = DeviceSerializer(device, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'device': device})
        serializer.save()
        return redirect('profile-list')