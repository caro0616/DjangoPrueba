from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='media/movie/images/')
    url = models.URLField(blank=True)
    year = models.IntegerField(default=2000) # Nuevo atributo
    genre = models.CharField(max_length=100, default="Desconocido")  # Nuevo atributo

    def __str__(self):
        return self.title

