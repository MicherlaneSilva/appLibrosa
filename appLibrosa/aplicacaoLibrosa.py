from PySimpleGUI import PySimpleGUI as sg
from telaGravacaoAudio import telaGravacao
from tocar import tocarAudio
from telaGraficos import telaGraficos

sound_file = "voz.wav"
#Layout
def telaPrincipal():
    sg.theme('Reddit')

    layout = [
        [sg.Button('GRAVAR', size=(7, 0)), sg.Button('OUVIR', size=(8, 0))],
        [sg.Button('GRÁFICOS', size=(20, 3))]
        
    ]
    #Janela

    janela = sg.Window('Librosa', layout, size=(200, 100), resizable=True)
    #Ler os eventos

    while True:
        eventos, valores = janela.read()

        if eventos == 'GRAVAR':
            telaGravacao()
        
        if eventos == 'GRÁFICOS':
            telaGraficos(sound_file)
            
        if eventos == 'OUVIR':
            tocarAudio(sound_file)

        if eventos == sg.WINDOW_CLOSED:
            break
            janela.close()

telaPrincipal()



        
