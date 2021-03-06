from django.shortcuts import render

from django.http import HttpResponse

class Tarefa(object):

    def __init__(self, titulo, data):
        self.titulo = titulo
        self.data = data

    def __str__(self):
        return self.titulo

def home(request):
    return HttpResponse("Olá")

def sobre(request):
    return HttpResponse("Fernanda Gomes")

def tarefa(request, numero):
    return HttpResponse("Tarefa: " + str(numero))

def tarefaN(request, ano, mes):
    return HttpResponse("Tarefa: " + str(ano) + "/" + str(mes))

def tarefaD(request, dia, mes, ano):
    return HttpResponse("Tarefa: " + str(dia) + "/" + str(mes) + "/" + str(ano))
