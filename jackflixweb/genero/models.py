from django.db import models

class Genero(models.Model):
    descricao = models.CharField('Gênero',max_length=50)

    def __str__(self):
        return self.descricao

