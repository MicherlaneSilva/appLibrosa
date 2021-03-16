from PySimpleGUI import PySimpleGUI as sg
from gravacaoAudioImagem import gravacao
#from test import gravarAudio
#from time import sleep
#from gravarTela import gravar


def telaGravacao():
    sg.theme('Reddit')

    layout = [
        [sg.Text('Tempo de gravação(s): '), sg.Input(size=(12, 5), key='tempo')],
        [sg.Button('Gravar'), sg.Button('Sair')]
    ]

    janela = sg.Window('Gravar WAV', layout, size=(200, 100))


    while True:
        eventos, valores = janela.read()

        if eventos == 'Gravar':
            tempo = int(valores['tempo'])
            #resultado = gravarAudio('voz', tempo)                
            resultado = gravacao('voz', tempo)
            if resultado:
                sg.popup('Resultado', 'Áudio gravado com sucesso!')
        
        if eventos == 'Sair':
            janela.close()
            
        if eventos == sg.WINDOW_CLOSED:
            break

    janela.close()




