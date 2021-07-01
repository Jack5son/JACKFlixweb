from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from . import forms
from . import models

def cadastro(request):
    form = forms.FilmeForm()
    if request.method == 'POST':
        print("Vou salvar os dados!")
        form = forms.FilmeForm(request.POST)

        if form.is_valid():
            print("Salvando")
            form.save(commit=True)
        else:
            print('error')
    filmes_list = models.Filme.objects.order_by('nome');
    data_dict = {'form': form, 'filme_records': filmes_list}
    return render(request, 'filme/filme.html', data_dict)


def delete(request, id):
    try:
        models.Filme.objects.filter(id=id).delete()
        form = forms.FilmeForm()
        filmes_list = models.Filme.objects.order_by('nome')
        data_dict = {'form': form, 'filme_records': filmes_list}
        return render(request, 'filme/filme.html', data_dict)
    except:
        return HttpResponseNotAllowed

def update(request, id):

    item = models.Filme.objects.get(id=id);
    if request.method == "GET":
        form = forms.FilmeForm(initial={"nome": item.nome,"idGenero": item.idGenero})
        data_dict = {'form': form}
        return render(request, 'filme/filme.upd.html', data_dict)

    else:
        form = forms.FilmeForm(request.POST)
        item.nome = form.data['nome']
        # Força adicionar o ID ("_id)
        item.idGenero_id = form.data['idGenero']
        item.save()
        form = forms.FilmeForm()
        filmes_list = models.Filme.objects.order_by('nome')
        data_dict = {'form': form, 'filme_records': filmes_list}
        return render(request, 'filme/filme.html', data_dict)
