import PySimpleGUI as psg
from main import get_quote
from aiRequest import ask

layout = [
    [psg.Text(text='Symbol: '), psg.Input(key='-SYMBOL-')],
    [psg.Button('Search')],
    [psg.Text(text='Tell Me About: '), psg.Input(key='-COMPANY-')],
    [psg.Button('Search')]
]

window = psg.Window('HelloWorld', layout, size=(715,250))

while True:
    event, values = window.read()
    if (values and '-SYMBOL-' in values and isinstance(values['-SYMBOL-'], str)):
        symbol = values['-SYMBOL-']
        if symbol:
            quote_data = get_quote(symbol.upper())
            print(quote_data)
    if (values and '-COMPANY-' in values and isinstance(values['-COMPANY-'], str)):
        symbol = values['-COMPANY-']
        if symbol:
            ai_response = ask(symbol.upper())
            print(ai_response)
    if event in (None, 'Exit'):
        break

window.close()