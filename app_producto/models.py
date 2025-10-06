from django.db import models

# Create your models here.
class producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    precio = models.IntegerField()
    #es para el administrador servidor admin
    def _str_(self):
        return f"{self.nombre} {self.precio}"
