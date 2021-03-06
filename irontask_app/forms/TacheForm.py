from django.forms import ModelForm
from django import forms
from irontask_app.models import Tache, Benevole


class TacheForm(ModelForm):
    nomTache = forms.CharField(label="Nom", widget=forms.TextInput({"type": "text", "class": "form-control",
                                                                    "id": "formGroupExampleInput",
                                                                    "placeholder": ""}))

    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "id": "message-text2", "rows": "3"}))

    dateDebut = forms.DateField(
        widget=forms.DateInput(attrs={"type": "text", "class": "form-control", "data-toggle": "datepicker"}))
    dateFin = forms.DateField(
        widget=forms.DateInput(attrs={"type": "text", "class": "form-control", "data-toggle": "datepicker"}))
    dateRappel = forms.DateField(
        widget=forms.DateInput(attrs={"type": "text", "class": "form-control", "data-toggle": "datepicker"}))

    niveauAvancement = forms.ChoiceField(choices=Tache.NIV_AVANCEMENT, widget=forms.Select(
        {"class": "custom-select", "id": "inputGroupSelect05 "}))
    niveauPriorite = forms.ChoiceField(choices=Tache.NIV_PRIORITE, widget=forms.Select(
        {"class": "custom-select", "id": "inputGroupSelect05 "}))

    responsable = forms.ModelChoiceField(label='Benevole', queryset=Benevole.objects.all(), widget=forms.Select(
        {"class": "custom-select", "id": "inputGroupSelect05 "}))

    class Meta:
        model = Tache
        exclude = {'fk_triathlon', 'dateAjout'}
