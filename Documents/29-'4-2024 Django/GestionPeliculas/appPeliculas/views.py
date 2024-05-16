from django.shortcuts import render, redirect

from appPeliculas.models import Genero, Pelicula

from django.views.decorators.csrf import csrf_protect, csrf_exempt

from django.conf import settings

import os








""" def vistaAgregarGenero(request):
     return render(request, "agregarGenero.html") """


def inicio(request):
    return render(request, "inicioDeSesion.html")


def agregarGenero(request):
    mensaje = ''  
    if request.method == 'POST':
        try:
            nombre = request.POST['txtGenero']
            genero = Genero.objects.create(
                nombre=nombre
                ),
            mensaje = 'Género agregado correctamente'
        except Exception as e:
            mensaje = "El genero ingresado ya existe en la Base de Datos"
    
    return render(request, 'agregarGenero.html', {'mensaje': mensaje}) 
    
    


def listarGeneros(request):
    generos = Genero.objects.all()
    retorno = {"generos": generos}
    return render(request, 'listarGeneros.html', retorno)


""" def consultarGeneroPorId(request, id):
    genero = Genero.objects.get(id = id)
    genero = Genero.objects.all()
    #Retornamos lo generos porque se necesitan en la interfaz
    retorno = {"genero": genero}
    return render (request, "actualizarGenero.html", retorno) """






def eliminarGenero(request, objectId):
    try:
        # Buscamos el genero por su ID
        generoEliminar = Genero.objects.get(id=objectId)
        # Eliminamos el genero
        generoEliminar.delete()
        
        mensaje = "Genero ELIMINADo correctamente"
        
    except Exception as error:  
        mensaje = str(error)
        
    retorno = {"mensaje": mensaje}
    
    return redirect("/listarGeneros/")
 
 

""" def vistaAgregarPelicula(request):
    generos= Genero.objects.all()
    retorno= {"generos": generos}
    return render(request, "agregarPelicula.html", retorno)
 """


def agregarPelicula(request):
    mensaje = ""

    if request.method == 'POST':
        try:
            codigo = request.POST['txtCodigo']
            titulo = request.POST['txtTitulo']
            protagonista = request.POST['txtProtagonista']
            duracion = int(request.POST['txtDuracion'])
            resumen = request.POST['txtResumen']
            foto = request.FILES['foto']  
            idGenero = int(request.POST['idGenero'])  
            genero = Genero.objects.get(id=idGenero)
            


            # Para guadar la nueva pelicula (pelicula.save() es reemplazado por: pelicula = Pelicula.objects.create )
            pelicula = Pelicula.objects.create(
                codigo=codigo,
                titulo=titulo,
                protagonista=protagonista,
                duracion=duracion,
                resumen=resumen,
                foto=foto,
                genero=genero
            )
            
            mensaje = "Pelicula agregada correctamente"
        except Exception as e:
            mensaje = str(e)
            pelicula = None

    # Obtener todos los géneros para pasarlos al formulario
    generos = Genero.objects.all()
    retorno = {"mensaje": mensaje, "generos": generos}
    return render(request, 'agregarPelicula.html', retorno) 


    

def listarPeliculas(request):
    peliculas = Pelicula.objects.all()
    retorno = {"peliculas": peliculas}
    return render(request, 'listarPeliculas.html', retorno)



def consultarPeliculaPorId(request, id):
    pelicula = Pelicula.objects.get(id = id)
    generos = Genero.objects.all()
    #Retornamos lo generos porque se necesitan en la interfaz
    retorno = {"pelicula": pelicula, "generos": generos}
    return render (request, "actualizarPelicula.html", retorno)




def actualizarPelicula(request):
    mensaje = ""  # Inicializamos la variable mensaje
    try:
        idPelicula = request.POST["idPelicula"]
        #Obtener la pelicula a partir de si ID
        peliculaActualizar = Pelicula.objects.get(id=idPelicula)
        #Actualizar los campos
        peliculaActualizar.codigo = request.POST["txtCodigo"]
        peliculaActualizar.titulo = request.POST["txtTitulo"]
        peliculaActualizar.protagonista = request.POST["txtProtagonista"]
        peliculaActualizar.duracion = request.POST["txtDuracion"]
        peliculaActualizar.resumen = request.POST["txtResumen"]
        idGenero = int(request.POST["idGenero"])
        #Obtner el objeto Genero a partir de su ID
        genero = Genero.objects.get(id=idGenero)
        peliculaActualizar.genero = genero
        foto = request.FILES.get("foto")
        
        
        
        #Si han enviado foto, se actualiza el campo
        if foto:
            #Primero eliminamos la foto existente
            if peliculaActualizar.foto:
                os.remove(os.path.join(settings.MEDIA_ROOT, str(peliculaActualizar.foto)))
            #Actualizamos con la nueva foto
            peliculaActualizar.foto = foto
            
        #Actualizar la pelicula en la base de datos
        peliculaActualizar.save()
        mensaje = "Pelicula Actualizada"
    except Exception as error:
        mensaje = str(error)
        
    retorno = {"mensaje": mensaje}
    
    
    """ return JsonResponse(retorno)  """
    
    return redirect("/listarPeliculas")    #Para que cuando se de click en "Actualizar, me lleve a la lista actualizada"
    
        

def eliminarPelicula(request, id):
    try:
        # Buscamos la pelicula por su ID
        peliculaEliminar = Pelicula.objects.get(id=id)
        # Eliminamos la Pelicula
        peliculaEliminar.delete()
        
        mensaje = "Pelicula ELIMINADA correctamente"
        
    except Exception as error:  
        mensaje = str(error)
        
    retorno = {"mensaje": mensaje}
    
    return redirect("/listarPeliculas/")
 
 










