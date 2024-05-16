from djongo import models

# Create your models here.

class Genero(models.Model):
    
    nombre = models.CharField(max_length=50, unique=True)



 # Esta funcion devuelve el un string(nombre) para poder visualizarlo en el admin
def __str__(self):
        return self.nombre    


class Pelicula(models.Model):
    codigo= models.CharField(max_length=9)
    titulo= models.CharField(max_length=50)
    protagonista= models.CharField(max_length=50)
    duracion= models.IntegerField()
    resumen= models.CharField(max_length=2000)
    foto = models.ImageField(upload_to="fotos/", null=True, blank=True)
    genero= models.ForeignKey(Genero, on_delete=models.PROTECT)  
    


 # Esta funcion devuelve el un string(titulo) para poder visualizarlo en el admin
def __str__(self) -> str:
        return self.titulo     
