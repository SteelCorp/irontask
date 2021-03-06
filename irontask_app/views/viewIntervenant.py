from django.shortcuts import render, redirect, get_object_or_404
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django_tables2 import RequestConfig

from irontask_app.forms.devisForms import DevisForm
from irontask_app.models import Intervenant, Triathlon
from django.urls import reverse
from irontask_app.forms.IntervenantForm import IntervenantForm
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from irontask_app.utils.decorators import triathlon_required
from irontask_app.utils.tables import IntervenantTables


@login_required(login_url='login/')
@triathlon_required
def listIntervenant(request):
    """Vue qui retourne la liste de tous les intervenant"""

    intervenant = Intervenant.objects.all()
    intervenantForm = IntervenantForm()
    devisForm = DevisForm()

    table = IntervenantTables(Intervenant.objects.all())
    RequestConfig(request, paginate={'per_page': 8}).configure(table)

    if request.method == 'POST':

        intervenantform = IntervenantForm(request.POST)

        if intervenantform.is_valid():
            intervenant = intervenantform.save(commit=True)
            intervenant.save()
        return render(request, 'personnels/Intervenant/listIntervenant.html',
                      {'Intervenant': intervenant, 'form': intervenantForm, 'table': table, 'devisForm': devisForm,
                       'successful_submit': True})

    return render(request, 'personnels/Intervenant/listIntervenant.html',
                  {'Intervenant': intervenant, 'form': intervenantForm, 'table': table, 'devisForm':devisForm, 'successful_submit': False})


@login_required(login_url='login/')
@triathlon_required
def ajouterDevis(request):
    tria = Triathlon.objects.get(id=request.session['idTriathlon'])
    if request.method == 'POST':
        devisForm = DevisForm(request.POST)
        print(devisForm.errors)
        if devisForm.is_valid():
            donation = devisForm.save(commit=False)
            donation.fk_triathlon = tria
            donation.save()
            return HttpResponseRedirect('/personnel/intervenant/')
        return HttpResponseRedirect('/personnel/intervenant/')

@login_required(login_url='login/')
@triathlon_required
def getIntervenant(request, siret):
    """
    Vue qui retourne l'intervenant fournit en paramètre
    :param siret est la primary key d'un intervenant
    """
    intervenant = Intervenant.objects.get(siret=siret)

    return render(request, "personnels/Intervenant/voirIntervenant.html", {'Intervenant': intervenant})


@login_required(login_url='login/')
@triathlon_required
def deleteIntervenant(request, siret):
    """Vue qui permet de supprimer un intervenant
    :param pk est la primary key d'un intervenant
    """
    Intervenant.objects.filter(siret=siret).delete()
    return redirect(reverse(viewname=listIntervenant))


@login_required(login_url='login/')
@triathlon_required
def createIntervenant(request):
    """ Vue qui permet de creer un intervenant
    """
    return render(request, 'personnel/add_Intervenant.html', {'IntervenantForm': IntervenantForm})

@login_required(login_url='login/')
@triathlon_required
def editerIntervenant(request, pk):
    """

    :param request:
    :param pk:
    :return:
    """
    inter = Intervenant.objects.get(pk=pk)
    intervenantForm = IntervenantForm(instance=inter)

    if request.method == "POST":
        form = IntervenantForm(request.POST, instance=inter)
        print(form.errors)

        if form.is_valid():
            form.save()

        return redirect('listIntervenant')

    return render(request, 'personnels/Intervenant/editerIntervenant.html', {'form': intervenantForm})
