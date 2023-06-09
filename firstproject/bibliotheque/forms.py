from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('titre', 'auteur', 'date_parution', 'nombre_pages','resume')
        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur') ,
            'date_parution' : _('date de parution'),
            'nombre_pages' : _('nombresde pages'),
            'resume' : _('Résumé')
        }
        localized_fields = ('date_parution',)