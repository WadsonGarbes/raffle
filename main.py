import PySimpleGUI as sg
from random import randint

sg.theme('Topanga')

layout = [
    [sg.Text('Rifa do Pedrinho - Insira o intervalo de números para rifar')],
    [sg.Text('Número inicial', size=(10, 1)), sg.InputText()],
    [sg.Text('Número final', size=(10, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
sg.popup("Eis o vencedor:", randint(int(values[0]), int(values[1])))
window.close()