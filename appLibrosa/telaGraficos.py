from PySimpleGUI import PySimpleGUI as sg
from graficos import exibirEspectrograma, exibirOscilograma

def telaGraficos(sound_file):
    sg.theme('Reddit')

    layout = [
        [sg.Button('ESPECTROGRAMA',size=(16,0)), sg.Button('OSCILOGRAMA', size=(26,0))]
    ]

    janela = sg.Window('Gráficos', layout, size=(300, 100))

    while True:
        eventos, valores = janela.read()

        if eventos == 'ESPECTROGRAMA':
            exibirEspectrograma(sound_file)
        
        if eventos == 'OSCILOGRAMA':
            exibirOscilograma(sound_file)
        
        if eventos == sg.WINDOW_CLOSED:
            break

    janela.close()


