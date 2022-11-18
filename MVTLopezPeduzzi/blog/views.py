from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Placas_de_video, Fuentes, Perifericos
from .forms import PlacasForm, FuentesForm, PerifericosForm


def mostrar_index(request):

    return render(request,"blog/index.html")

def mostrar_bienvenida(request):
    
    return render(request, "blog/bienvenida.html")



def mostrar_placa(request):

    if request.method == "POST":

        formulario = PlacasForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


        Placas = Placas_de_video(nombre=formulario_limpio ["nombre"], marca=formulario_limpio ["marca"])

        Placas.save()

        return render(request, "blog/index.html")
    
    else:
        formulario = PlacasForm()

 
    return render (request, "blog/mostrar_placa.html", {"formulario": formulario})

def mostrar_fuente(request):

    if request.method == "POST":

        formulario = FuentesForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


        Fuente = Fuentes(Watts=formulario_limpio ["Watts"], marca=formulario_limpio ["marca"])

        Fuente.save()

        return render(request, "blog/index.html")
    
    else:
        formulario = FuentesForm()

 
    return render (request, "blog/mostrar_fuente.html", {"formulario": formulario})

def mostrar_perifericos(request):

    if request.method == "POST":

        formulario = PerifericosForm(request.POST)

        if formulario.is_valid():

            formulario_limpio = formulario.cleaned_data


        Periferico = Perifericos(tipo=formulario_limpio ["tipo"], marca=formulario_limpio ["marca"], modelo=formulario_limpio ["modelo"])

        Periferico.save()

        return render(request, "blog/index.html")
    
    else:
        formulario = PerifericosForm()

 
    return render (request, "blog/mostrar_perifericos.html", {"formulario": formulario})

def buscar_componentes(request):

    data = request.GET.get("marca", "")
    error = ""
    if data :
        try:
            componentes = Fuentes.objects.get(marca = data)

            return render (request, "blog/buscar_componentes.html", {"marca" : data , "componentes" : componentes})

        except Exception as exc:
            error = "No hay componentes en stock"
    
    return render (request, "blog/buscar_componentes.html", {"error" : error})

def mostrar_placas(request):

    tarjeta = Placas_de_video.objects.all()

    context = {"tarjeta": tarjeta}

    return render (request, "blog/mostrar_placas.html", context=context)

def eliminar_placas(request, placa_id):

    placas = Placas_de_video.objects.get(id= placa_id)

    placas.delete()

    tarjeta = Placas_de_video.objects.all()

    context = {"tarjeta": tarjeta}

    return render (request, "blog/mostrar_placas.html", context=context)



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

class PlacaList(ListView):

    model = Placas_de_video
    template_name = "blog/placas_list.html"


class PlacaDetailView(DetailView):
    model = Placas_de_video
    template_name = "blog/placas_detalle.html"



