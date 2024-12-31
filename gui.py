import PySimpleGUI as psg
from main import get_quote

layout = [
    [psg.Text(text='Symbol: '), psg.Input(key='-SYMBOL-')],
    [psg.Button('Search')]
]

window = psg.Window('HelloWorld', layout, size=(715,250))

while True:
    event, values = window.read()
    if (values and '-SYMBOL-' in values and isinstance(values['-SYMBOL-'], str)):
        symbol = values['-SYMBOL-']
        quote_data = get_quote(symbol.upper())
        print(quote_data)
    if event in (None, 'Exit'):
        break

window.close()