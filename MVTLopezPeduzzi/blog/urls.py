from django.urls import path
from blog import views
urlpatterns = [
    path("index/", views.mostrar_index, name ="Home"),
    path("bienvenida/", views.mostrar_bienvenida),
    path("placas/", views.mostrar_placa, name="Placas de video"),
    path("fuentes/", views.mostrar_fuente, name="Fuentes"),
    path("perifericos/", views.mostrar_perifericos, name="Perifericos"),
    path("componentes/", views.buscar_componentes, name="Buscar componentes"),
    path("mostrarplaca/", views.mostrar_placas, name="Placas en Stock"),
    path("eliminarplaca/<placa_id>", views.eliminar_placas, name="Eliminar Placas"),
    path("actualizarplaca/<placa_id>", views.actualizar_placa, name="Actualizar Placas"),
    path("listaplacas/", views.PlacaList.as_view(), name="List"),
    path("detalleplacas/<pk>", views.PlacaDetailView.as_view(), name="Detail"),
    path("signup/", views.SignUpVieW.as_view(), name="Sign Up"),
    path("login/", views.AdminLoginView.as_view(), name="Login"),
    path("logout/", views.AdminLogoutView.as_view(), name = "Logout"),
    path("editar_usuario/", views.editar_usuario, name="Editar Usuario"),
]
