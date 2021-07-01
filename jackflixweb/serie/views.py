from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

def cadastro(request):
    form = forms.SerieForm()
    if request.method == 'POST':
        print("Vou salvar os dados!")
        form = forms.SerieForm(request.POST)

        if form.is_valid():
            print("Salvando")
            form.save(commit=True)
        else:
            print('error')
    series_list = models.Serie.objects.order_by('nome');
    data_dict = {'form': form, 'serie_records': series_list}
    return render(request, 'serie/serie.html', data_dict)


def delete(request, id):
    try:
        models.Serie.objects.filter(id=id).delete()
        form = forms.SerieForm()
        series_list = models.Serie.objects.order_by('nome')
        data_dict = {'form': form, 'serie_records': series_list}
        return render(request, 'serie/serie.html', data_dict)
    except:
        return HttpResponseNotAllowed

def update(request, id):

    item = models.Serie.objects.get(id=id);
    if request.method == "GET":
        form = forms.SerieForm(initial={"nome": item.nome,"idGenero": item.idGenero})
        data_dict = {'form': form}
        return render(request, 'serie/serie.upd.html', data_dict)

    else:
        form = forms.SerieForm(request.POST)
        item.nome = form.data['nome']
        # Força adicionar o ID ("_id)
        item.idGenero_id = form.data['idGenero']
        item.save()
        form = forms.SerieForm()
        series_list = models.Serie.objects.order_by('nome')
        data_dict = {'form': form, 'serie_records': series_list}
        return render(request, 'serie/serie.html', data_dict)
