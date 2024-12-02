document.addEventListener('DOMContentLoaded', function() {
    // Obtener todos los elementos de proyecto
    const projectItems = document.querySelectorAll('.project-item');

    // Configurar un listener de evento para cada proyecto
    projectItems.forEach(item => {
        item.addEventListener('click', function() {
            // Obtener el ID del proyecto
            const projectId = item.getAttribute('data-id');

            // Llamar a la API para obtener los detalles del proyecto
            fetch(`/api/proyectos/${projectId}/`)
                .then(response => response.json())
                .then(data => {
                    // Mostrar los detalles del proyecto
                    document.getElementById('project-name').textContent = `Nombre: ${data.nombre}`;
                    document.getElementById('project-rut').textContent = `RUT de los Integrantes: ${data.rut}`;
                    document.getElementById('project-integrantes').textContent = `Integrantes: ${data.integrantes}`;

                    // Mostrar los botones de editar y eliminar
                    document.getElementById('edit-button').style.display = 'inline-block';
                    document.getElementById('delete-button').style.display = 'inline-block';

                    // Actualizar las URLs de los botones de editar y eliminar
                    document.getElementById('edit-button').onclick = function() {
                        window.location.href = `/editar_proyecto/${data.id}/`;
                    };

                    document.getElementById('delete-button').onclick = function() {
                        if (confirm('¿Estás seguro de que quieres eliminar este proyecto?')) {
                            fetch(`/eliminar_proyecto/${data.id}/`, {
                                method: 'DELETE'
                            })
                            .then(response => {
                                if (response.ok) {
                                    alert('Proyecto eliminado');
                                    window.location.reload(); // Recargar la página después de eliminar
                                } else {
                                    alert('Error al eliminar el proyecto');
                                }
                            });
                        }
                    };

                    // Mostrar los detalles
                    document.getElementById('project-details').style.display = 'block';
                })
                .catch(error => {
                    console.error('Error al obtener los detalles del proyecto:', error);
                });
        });
    });
});
