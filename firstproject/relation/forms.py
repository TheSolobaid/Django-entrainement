from django.forms import ModelForm, ChoiceField, ValidationError
from django.utils.translation import gettext_lazy as _
from . import models

class Marque_Form(ModelForm):
    class Meta:
        model = models.marque
        fields = ('nom', 'pays','createur')
        labels = {
            'nom': _('Nom'),
            'pays': _("Pays d'orrigine"),
            'createur': _('Créateur')
        }

class Auto_Form(ModelForm):
    class Meta:
        model = models.auto
        fields = ("nom","puissance", 'marque',)
        labels = {
            'nom': _("Nom du model"),
            'puissance': _('Puissance de votre véhicule'),
            'marque': _("Choisissez la marque"),
        }
