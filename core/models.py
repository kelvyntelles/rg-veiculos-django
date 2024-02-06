from django.db import models


class Banner(models.Model):
    titulo = models.CharField(max_length=50)
    imagem = models.ImageField()

    def __str__(self):
        return self.titulo


class Agendamento(models.Model):
    nome_cliente = models.CharField(max_length=100)
    telefone_cliente = models.CharField(max_length=20)
    modelo_carro = models.CharField(max_length=100)
    ano_carro = models.IntegerField()
    tipo_servico = models.CharField(max_length=50)
    descricao_servico = models.TextField()
    data_agendamento = models.DateField()

    def __str__(self):
        return self.nome_cliente


class Carro(models.Model):
    imagem_capa = models.ImageField()
    marca = models.CharField(default="Fiat", max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    descricao = models.TextField()
    km_rodados = models.FloatField()
    valor = models.FloatField()

    def __str__(self):
        return self.modelo


class ImagemCarro(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField()

    def __str__(self):
        return f"Imagem de {self.carro}"

