from django.db import models

# Create your models here.

#son 5 motores, cada uno con 2 pines INPUT y 2 pines OUTPUT
#pines input (encoders); pines output (ENABLE y DIR)

class motores(models.Model):
    name=models.CharField(max_length=5)
    ena=models.IntegerField() #enable (True=detenido)
    di=models.IntegerField() #direction
    encA=models.IntegerField() #encoder A
    encB=models.IntegerField() #encoder B
    