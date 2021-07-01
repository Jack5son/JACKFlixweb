from django.db import models


# Create your models here.
class Filme(models.Model):
    nome = models.CharField('Título do filme', max_length=150)
    idGenero = models.ForeignKey('genero.Genero', verbose_name="Gênero", on_delete=models.PROTECT)

    def __str__(self):
        return self.nome
