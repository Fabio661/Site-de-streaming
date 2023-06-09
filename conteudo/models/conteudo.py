from embed_video.fields import EmbedVideoField
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

STATUS = (
    ('Bem Avaliado', 'Bem Avaliado'),
    ('Normal', 'Normal')
)

GENERO = (
    ('Filme', 'Filme'),
    ('Serie', 'Serie')
)

GENERO_CINEMATOGRAFICO = (
    ('Acao', 'Acao'), ('Aventura', 'Aventura'), ('Comedia', 'Comedia'), ('Documentario', 'Documentario'), ('Drama', 'Drama'), 
    ('Fantasia', 'Fantasia'), ('Musical', 'Musical'), ('Terror', 'Terror'), ('Romance', 'Romance'), ('Ficcao', 'Ficcao')
)

class Conteudo(models.Model):
    titulo = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    imagem = models.ImageField(upload_to='imagems/')
    sinopse = models.TextField()
    url = EmbedVideoField(blank=True)
    elenco = models.CharField(max_length=100, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    idade_recomendada = models.IntegerField(validators=[MinValueValidator(10),
                                                        MaxValueValidator(18)])
    likes = models.ManyToManyField(User, blank=True, related_name='like_post')
    salvo = models.ManyToManyField(User, blank=True, related_name='salvar_post')
    status = models.CharField(max_length=12, choices=STATUS, default='Normal')
    genero = models.CharField(max_length=5, choices=GENERO)
    genero_cinematografico = models.CharField(max_length=12, choices=GENERO_CINEMATOGRAFICO)
    
    class Meta:
        ordering = ['-criado_em']
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.titulo