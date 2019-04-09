#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from random import randint
from random import choice

print('''
┬ ┬┌─┐┬  ┌─┐┌─┐┌┬┐┌─┐  ╔╦╗┬─┐   ╔╦╗┌─┐┬─┐┌─┐┬ ┬┌─┐
│││├┤ │  │  │ ││││├┤   ║║║├┬┘   ║║║├─┤├┬┘│  │ │└─┐
└┴┘└─┘┴─┘└─┘└─┘┴ ┴└─┘  ╩ ╩┴└─o  ╩ ╩┴ ┴┴└─└─┘└─┘└─┘
''')
sleep(2)

def rotina():

    print('▬'*40)
    print('progamas de atividades de rotinas. V1')
    print('▬'*40)

    turno = int(input('Selecione qual turno deseja progamas sua rotina ?\n[0]Manhã\n[1]Tarde\n[2]Noite\n'))

    if turno == 0:
        def manha():
            lista = ['Ouvir musica para acordar','fazer exercicios ou trabalhos se tiver']#exemplos porque que ainda vou ter que colocar
            print('Primeiro tenha um bom café ..')
            sleep(2)
            escolha = choice(lista)
            print('Na parte da manha você deve '+escolha)
            sleep(2)
        manha()

    if turno == 1:
        def tarde():
            lista = ['Jogar','Ver algum filme']
            print('Não escqueca do almoço reforçado')
            sleep(2)
            escolha = choice(lista)
            print('A Tarde voce deve '+escolha)
            sleep(2)
        tarde()

    if turno == 2:
        def noite():
            lista = ['Jogar','Ver algum filme','Ouvir música pós faculdade para relaxar']
            print('Chegando a noite pós faculdade\nfaça um lanche da noite ou jante')
            sleep(2)
            escolha = choice(lista)
            print('A noite você deve '+escolha)
            sleep(2)
        noite()

rotina()

def restart():
    while True:
        pergunta = int(input('Deseja dar um restart ?\n(0) para Sim\n(1) para Não\n'))
        if pergunta == 0:
            rotina()

        if pergunta == 1:
            print('Até logo ..')
            sleep(1)
            print('saindo ..')
            sleep(1)
            break

restart()
