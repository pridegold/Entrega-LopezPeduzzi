from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Avatar,Placas_de_video, Fuentes, Perifericos
from .forms import UserEditForm, PlacasForm, FuentesForm, PerifericosForm, SignUpForm
#redireccion
from django.urls import reverse_lazy
#Aut
from django.contrib.auth.views import LoginView, LogoutView
#Decorados sirven para funciones
from django.contrib.auth.decorators import login_required
#mixins sirven para las clases 
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime


def mostrar_index(request):

    imagenes = Avatar.objects.filter(user=request.user.id)

    return render(request,"blog/index.html", {"url": imagenes[0].imagen.url})

def mostrar_bienvenida(request):
    
    return render(request, "blog/bienvenida.html")


@login_required
def mostrar_placa(request):
    currentdate = datetime.datetime.today()
    if request.method == "POST":

        formulario = PlacasForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


        Placas = Placas_de_video(nombre=formulario_limpio ["nombre"], marca=formulario_limpio ["marca"])

        Placas.save()

        return render(request, "blog/index.html")
    
    else:
        formulario = PlacasForm()

 
    return render (request, "blog/mostrar_placa.html", {"formulario": formulario, "currentdate" : currentdate})
@login_required
def mostrar_fuente(request):
    currentdate = datetime.datetime.today()

    if request.method == "POST":

        formulario = FuentesForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


        Fuente = Fuentes(Watts=formulario_limpio ["Watts"], marca=formulario_limpio ["marca"])

        Fuente.save()

        return render(request, "blog/index.html")
    
    else:
        formulario = FuentesForm()

 
    return render (request, "blog/mostrar_fuente.html", {"formulario": formulario, "currentdate" : currentdate})
@login_required
def mostrar_perifericos(request):
    currentdate = datetime.datetime.today()

    if request.method == "POST":

        formulario = PerifericosForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


        Periferico = Perifericos(tipo=formulario_limpio ["tipo"], marca=formulario_limpio ["marca"], modelo=formulario_limpio ["modelo"])

        Periferico.save()

        return render(request, "blog/index.html")
    
    else:
        formulario = PerifericosForm()

 
    return render (request, "blog/mostrar_perifericos.html", {"formulario": formulario, "currentdate" : currentdate})

def buscar_componentes(request):
    currentdate = datetime.datetime.today()
    data = request.GET.get("marca", "")
    error = ""
    if data :
        try:
            componentes = Placas_de_video.objects.get(marca = data)

            return render (request, "blog/buscar_componentes.html", {"marca" : data , "componentes" : componentes , "currentdate" : currentdate})

        except Exception as exc:
            error = "No hay componentes en stock"
    
    return render (request, "blog/buscar_componentes.html", {"error" : error})

def buscar_componentes1(request):
    currentdate = datetime.datetime.today()
    data = request.GET.get("marca", "")
    error = ""
    if data :
        try:
            componentes = Fuentes.objects.get(marca = data)

            return render (request, "blog/buscar_componentes1.html", {"marca" : data , "componentes" : componentes , "currentdate" : currentdate})

        except Exception as exc:
            error = "No hay componentes en stock"
    
    return render (request, "blog/buscar_componentes1.html", {"error" : error})

def buscar_componentes2(request):
    currentdate = datetime.datetime.today()
    data = request.GET.get("marca", "")
    error = ""
    if data :
        try:
            componentes = Perifericos.objects.get(marca = data)

            return render (request, "blog/buscar_componentes2.html", {"marca" : data , "componentes" : componentes , "currentdate" : currentdate})

        except Exception as exc:
            error = "No hay componentes en stock"
    
    return render (request, "blog/buscar_componentes2.html", {"error" : error})

def mostrar_placas(request):

    tarjeta = Placas_de_video.objects.all()
    context = {"tarjeta": tarjeta}
    
    

    return render (request, "blog/mostrar_placas.html",context)
@login_required
def eliminar_placas(request, placa_id):

    placas = Placas_de_video.objects.get(id= placa_id)

    placas.delete()

    tarjeta = Placas_de_video.objects.all()

    context = {"tarjeta": tarjeta}

    return render (request, "blog/mostrar_placas.html", context=context)


@login_required
def actualizar_placa(request, placa_id):

    Placas = Placas_de_video.objects.get(id= placa_id)

    if request.method == "POST":

        formulario = PlacasForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data

        Placas.nombre = formulario_limpio["nombre"]
        Placas.marca = formulario_limpio["marca"]
       
       
       
        Placas.save()

        return render(request, "blog/index.html")
    else:
        formulario = PlacasForm(initial={"nombre": Placas.nombre, "marca": Placas.marca})

        return render (request, "blog/actualizar_placa.html", {"formulario": formulario})

def editar_usuario(request):

    usuario = request.user

    if request.method == "POST":
        usuario_form = UserEditForm(request.POST)
        
        if usuario_form.is_valid():

            informacion = usuario_form.cleaned_data

            usuario.username = informacion["username"]
            usuario.email = informacion["email"]
            usuario.password1 = informacion["password1"]
            usuario.password2 = informacion["password2"]

            usuario.save()

            return render(request, "blog/index.html")



        
    else:
        usuario_form = UserEditForm(initial={
            "username": usuario.username,
            "email": usuario.email,
        })
    return render(request, "blog/admin_update.html", {
        "form": usuario_form,
        "usuario": usuario
    })

def mostrar_pages(request):

    return render (request, "blog/pages.html")

def mostrar_about(request):

    return render (request, "blog/about.html")

def no_disponible(request):

    return render (request, "blog/nodisponible.html")
class PlacaList(LoginRequiredMixin, ListView):

    model = Placas_de_video
    template_name = "blog/placas_list.html"


class PlacaDetailView(DetailView):
    model = Placas_de_video
    template_name = "blog/placas_detalle.html"


class SignUpVieW(CreateView):

    form_class = SignUpForm
    success_url = reverse_lazy("Bienvenida")
    template_name = "blog/registro.html"



class AdminLoginView(LoginView):

    template_name = "blog/login.html"

class AdminLogoutView(LogoutView):

    template_name = "blog/logout.html"



    


