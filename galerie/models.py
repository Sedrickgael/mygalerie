from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contenu(models.Model):
    """Model definition for Contenu."""
    SPORT='Sport'
    CINEMA='Cinema'
    ECONOMIE='Economie'
    POLITIQUE='Politique'
    AUTOMOBILE='Automobile'
    HIGHTECH='Hightech'
    MUSIQUE='Musique'
    DIVERTISSEMENT='Divertissement'
    VOYAGE='Voyage'
    CATEGORIE=[
        (SPORT, 'Sport'),
        (CINEMA, 'Cinema'),
        (ECONOMIE,'Economie'),
        (POLITIQUE,'Politique'),
        (AUTOMOBILE, 'Automobile'),
        (HIGHTECH, 'Hightech'),
        (MUSIQUE, 'Musique'),
        (DIVERTISSEMENT, 'Divertissement'),
        (VOYAGE, 'Voyage'),
    ]
    
    categorie = models.CharField(
        max_length=30,
        choices=CATEGORIE,
    )
    description = models.TextField()
    etiquette = models.CharField( max_length=50)
    user = models.ForeignKey(User, verbose_name='Utilisateur', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/contenu/%Y/%m/%d/')
    date_add = models.DateTimeField( auto_now_add=True)
    date_update = models.DateTimeField( auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        """Meta definition for Contenu."""

        verbose_name = 'Contenu'
        verbose_name_plural = 'Contenus'

    def __str__(self):
        """Unicode representation of Contenu."""
        return self.user.username + ' '+ self.description

