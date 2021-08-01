from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    rut = models.CharField(max_length=10)

class Tour(models.Model):
    nombre=models.CharField(max_length=60)
    dias=models.IntegerField()
    tours=models.Manager()
    def __str__(self):
        return self.nombre
class TourFactory:
    def __init__(self):
        self.tours=[]
        self.tours.append(Tour(1,"Valle de la luna", 5))
        self.tours.append(Tour(2,"Torres del Paine",15))

    def obtener_tours(self):
        return self.tours

    def getTour(self,id):
        for tour in self.tours:
            if tour.id==id:
                return tour
        return None
class TourFacade:
    def __init__(self):
        self.tourFatory=Tour.tours

    def buscarTours(self):
        return self.tourFatory.all()

    def buscarTour(self,id):
        return self.tourFatory.get(id=id)




# Create your models here.
