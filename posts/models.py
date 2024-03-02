from django.db import models

# Create your models here.
# Aqui estamos creando el cuadro en el cual podremos agregar cada post en el navegador
class Post(models.Model):
    text = models.TextField()
# esta sentencia es para que muestre los primeros 50 caracteres en la lista de post que se hayan hecho
    def __str__(self):
        return self.text[:50]