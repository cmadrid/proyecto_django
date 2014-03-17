from django.db import models


class Marca(models.Model):
    nombre  =   models.CharField(max_length=50)
    codigo_propio   =   models.Model(max_length=50)
    
class GrupoItem(models.Model):
    nombre  =   models.CharField(max_length=50)
    
class Bodega(models.Model):
    nombre  = models.CharField(max_length=50)
    direccion   = models.Model(max_length=50)
    
    

class Item(models.Model):
    codigo_barras   = models.CharField(max_length=50)
    codigo_propio   = models.CharField(max_length=30)
    descripcion     = models.CharField(max_length=200)
    es_bien         = models.BooleanField(initial=False)
    es_servicio     = models.BooleanField(initial=False)
   
    
