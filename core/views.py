from django.shortcuts import render, redirect
from .models import Carro, Banner, Agendamento
import random
from django.contrib.messages import constants
from django.contrib import messages
from django.http import Http404


def home(request):
    todos_carros = Carro.objects.all()
    todos_banners = Banner.objects.all()

    carros_aleatorios = random.sample(list(todos_carros), 4)
    banners_aleatorios = random.sample(list(todos_banners), 2)

    context = {'carros': carros_aleatorios, 'banners': banners_aleatorios}
    return render(request, 'home.html', context)


def carros(request):
    todos_carros = Carro.objects.all()
    todos_banners = Banner.objects.all()

    banners_aleatorios = random.sample(list(todos_banners), 2)

    context = {'carros': todos_carros, 'banners': banners_aleatorios}
    return render(request, 'carros.html', context)


def carro(request, id):
    carro = Carro.objects.get(id=id)

    if not carro.id == id:
        raise Http404()

    if request.method == 'GET':
        return render(request, 'carro.html', {
            'carro': carro,
        })


def agendar_servico(request):
    if request.method == 'GET':
        return render(request, 'agendar-servico.html')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        modelo = request.POST.get('modelo')
        ano = request.POST.get('ano')
        tipo_servico = request.POST.get('tipo_servico')
        data = request.POST.get('data')
        descricao = request.POST.get('descricao')

        if len(nome) <= 1:
            messages.add_message(
                request, constants.WARNING, 'Informe seu nome'
            )
            return redirect('/agendar-servico')

        if len(telefone) <= 10:
            messages.add_message(
                request, constants.WARNING, 'Telefone invalido'
            )
            return redirect('/agendar-servico')

        if len(modelo) <= 3:
            messages.add_message(
                request, constants.WARNING, 'Modelo do carro não informado'
            )
            return redirect('/agendar-servico')

        if len(ano) <= 3:
            messages.add_message(
                request, constants.WARNING, 'Informe o ano do seu carro'
            )
            return redirect('/agendar-servico')

        if len(tipo_servico) <= 1:
            messages.add_message(
                request, constants.WARNING, 'Tipo de serviço não informado'
            )
            return redirect('/agendar-servico')

        if len(data) <= 1:
            messages.add_message(
                request, constants.WARNING, 'Data do agendamento não informado'
            )
            return redirect('/agendar-servico')

        agendamento = Agendamento(
            nome_cliente=nome,
            telefone_cliente=telefone,
            modelo_carro=modelo,
            ano_carro=ano,
            tipo_servico=tipo_servico,
            descricao_servico=descricao,
            data_agendamento=data,
        )
        agendamento.save()

        messages.add_message(
            request, constants.SUCCESS, 'Agendamento solicitado com sucesso'
        )

        return redirect('/agendar-servico')


def contato(request):
    return render(request, 'contato.html')
