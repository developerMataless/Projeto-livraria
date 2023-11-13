from django.db import models


class Livro(models.Model):
    """
    Modelo para representar um livro.
    """

    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    editora = models.CharField(max_length=255)
    paginas = models.IntegerField()
    categoria = models.CharField(max_length=255)


class Exemplar(models.Model):
    """
    Modelo para representar um exemplar de um livro.
    """

    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=(
        ('disponivel', 'Disponível'),
        ('emprestado', 'Emprestado'),
    ))