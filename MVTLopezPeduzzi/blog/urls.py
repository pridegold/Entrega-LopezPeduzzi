from django.urls import path
from blog import views
urlpatterns = [
    path("index/", views.mostrar_index, name ="Home"),
    path("bienvenida/", views.mostrar_bienvenida),
    path("placas/", views.mostrar_placa, name="Ingresar Placa de Video a BD"),
    path("fuentes/", views.mostrar_fuente, name="Fuentes"),
    path("perifericos/", views.mostrar_perifericos, name="Perifericos"),
    path("componentes/", views.buscar_componentes, name="Placas de Video en Stock"),
    path("componentes1/", views.buscar_componentes1, name="Fuentes en Stock"),
    path("componentes2/", views.buscar_componentes2, name="Perifericos en Stock"),
    path("mostrarplaca/", views.mostrar_placas, name="Disponibilidad Inmediata"),
    path("eliminarplaca/<placa_id>", views.eliminar_placas, name="Eliminar Placas"),
    path("actualizarplaca/<placa_id>", views.actualizar_placa, name="Actualizar Placas"),
    path("listaplacas/", views.PlacaList.as_view(), name="List"),
    path("detalleplacas/<pk>", views.PlacaDetailView.as_view(), name="Detail"),
    path("signup/", views.SignUpVieW.as_view(), name="Sign Up"),
    path("login/", views.AdminLoginView.as_view(), name="Login"),
    path("logout/", views.AdminLogoutView.as_view(), name = "Logout"),
    path("editar_usuario/", views.editar_usuario, name="Editar Usuario"),
    path("pages/", views.mostrar_pages, name= "Pages"),
]
