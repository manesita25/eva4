from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Proyecto
from .serializers import ProyectoSerializer
from rest_framework import viewsets 
import json


# Definición del ProyectoViewSet
class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()  # Consulta para obtener todos los proyectos
    serializer_class = ProyectoSerializer  # Asegúrate de tener un ProyectoSerializer
# Vista para la lista de proyectos
def proyectos_lista(request):
    proyectos = Proyecto.objects.all()  # Obtener todos los proyectos
    return render(request, 'proyectos.html', {'proyectos': proyectos})

# Vista para agregar un nuevo proyecto
def agregar_proyecto(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        rut = request.POST.get('rut')
        integrantes = request.POST.get('integrantes')

        # Crear y guardar el nuevo proyecto
        nuevo_proyecto = Proyecto(
            nombre=nombre,
            rut=rut,
            integrantes=integrantes
        )
        nuevo_proyecto.save()

        # Redirigir a la lista de proyectos después de guardar
        return redirect('proyectos_lista')

    return render(request, 'agregar_proyecto.html')

# Vista para editar un proyecto existente
def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        # Actualizar los datos del proyecto con los valores enviados en el formulario
        proyecto.nombre = request.POST.get('nombre')
        proyecto.rut = request.POST.get('rut')
        proyecto.integrantes = request.POST.get('integrantes')
        proyecto.save()
        return redirect('proyectos_lista')

    # Renderizar el formulario de edición con los datos actuales del proyecto
    return render(request, 'editar_proyecto.html', {'proyecto': proyecto})

# Vista para eliminar un proyecto
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    if request.method == 'POST':
        # Eliminar el proyecto y redirigir a la lista de proyectos
        proyecto.delete()
        return redirect('proyectos_lista')

    # Renderizar la página de confirmación de eliminación
    return render(request, 'eliminar_proyecto.html', {'proyecto': proyecto})

# API para manejar proyectos (GET y POST)
def api_proyectos(request):
    if request.method == 'GET':
        # Obtener todos los proyectos y devolverlos en formato JSON
        proyectos = Proyecto.objects.all().values('nombre', 'rut', 'integrantes')
        return JsonResponse(list(proyectos), safe=False)

    if request.method == 'POST':
        # Obtener los datos del cuerpo de la solicitud (JSON)
        data = json.loads(request.body)
        
        # Crear un nuevo proyecto con los datos recibidos
        proyecto = Proyecto.objects.create(
            nombre=data['nombre'],
            rut=data['rut'],  # Asegúrate de que 'rut' coincide con el nombre del campo en el modelo
            integrantes=data['integrantes']
        )

        # Retornar una respuesta con el ID del nuevo proyecto creado
        return JsonResponse({'id': proyecto.id}, status=201)

