from PySimpleGUI import PySimpleGUI as sg

sg.Theme('Dark')

layout  = [
    [sg.Button('Gravar'), sg.Button('Parar')]
]

janela = sg.Window('Gravação', layout)

while True:
    eventos, valores = janela.read()