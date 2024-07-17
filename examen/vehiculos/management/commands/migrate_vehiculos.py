import requests
from django.core.management.base import BaseCommand
from vehiculos.models import Vehiculoo

class Command(BaseCommand):
    help = 'Migrate data from API to Vehiculoo model'

    def handle(self, *args, **kwargs):
        api_url = "http://localhost:3000/api/vehiculos"
        response = requests.get(api_url)

        if response.status_code == 200:
            vehiculos_data = response.json()
            for vehiculo_data in vehiculos_data:
                Vehiculoo.objects.create(
                    nombre=vehiculo_data['nombre'],
                    descripcion=vehiculo_data['descripcion'],
                    precio=vehiculo_data['precio'],
                    imagen=vehiculo_data['imagen']
                )
            self.stdout.write(self.style.SUCCESS('Datos migrados con éxito a Vehiculoo.'))
        else:
            self.stdout.write(self.style.ERROR('Error al obtener los datos de la API.'))
