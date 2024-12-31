import PySimpleGUI as psg
from main import get_quote
from aiRequest import ask

layout = [
    [psg.Text(text='Symbol: '), psg.Input(key='-SYMBOL-', do_not_clear=False)],
    [psg.Button('Search')],
    [psg.Text("", size=(30, 5), key='-QUOTE-', visible=False)],
    [psg.Text(text='Tell Me About: '), psg.Input(key='-COMPANY-', do_not_clear=False)],
    [psg.Button('Search')],
    [psg.Multiline(size=(80, 30), key='-OUTPUT-', autoscroll=True, visible=False)]
]

window = psg.Window('HelloWorld', layout, size=(715, 500))

while True:
    event, values = window.read()
    if (values and '-SYMBOL-' in values and isinstance(values['-SYMBOL-'], str)):
        window['-QUOTE-'].update(value='', visible=False)
        symbol = values['-SYMBOL-']
        if symbol:
            quote_data = get_quote(symbol.upper())
            window['-QUOTE-'].update(value=quote_data, visible=True)
    if (values and '-COMPANY-' in values and isinstance(values['-COMPANY-'], str)):
        window['-OUTPUT-'].update(value='', visible=False)
        symbol = values['-COMPANY-']
        if symbol:
            ai_response = ask(symbol.upper())
            window['-OUTPUT-'].update(value=ai_response, visible=True)
    if event in (None, 'Exit'):
        break

window.close()