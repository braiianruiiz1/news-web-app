from django.db import models
from ckeditor.fields import RichTextField

class New(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    description = RichTextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", blank=True, null=True, upload_to='news')
    author = models.CharField(verbose_name="Autor", max_length=200)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "noticia"
        verbose_name_plural = "noticias"
        ordering = ['-created']
        
    def __str__(self):
        return self.title