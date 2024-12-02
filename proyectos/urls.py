from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProyectoViewSet
from .views import proyectos_lista, agregar_proyecto, editar_proyecto, eliminar_proyecto
from . import views

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    path('', views.proyectos_lista, name='proyectos_lista'),  # Ruta para el frontend (HTML)
    path('agregar/', views.agregar_proyecto, name='agregar_proyecto'),
    path('editar/<int:proyecto_id>/', views.editar_proyecto, name ='editar_proyecto'),
    path('eliminar/<int:proyecto_id>/', views.eliminar_proyecto, name='eliminar_proyecto'),
]