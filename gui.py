import PySimpleGUI as psg
from quote import get_quote
from aiRequest import ask

layoutOne = [
    [psg.Button('Company Search', key='Company_Pane')],
    [psg.Text('Get Quote')],
    [psg.Text(text='Symbol: '), psg.Input(key='-SYMBOL-', do_not_clear=False)],
    [psg.Button('Search', key="Fetch_Quote")],
    [psg.Text("", size=(30, 5), key='-QUOTE-', visible=False)],
]

layoutTwo = [
    [psg.Button('Quote Search', key='Quotes_Pane')],
    [psg.Text('Get details on a company')],
    [psg.Text(text='Symbol: '), psg.Input(key='-COMPANY-', do_not_clear=False)],
    [psg.Button('Search', key="Search_Company")],
    [psg.Multiline(size=(80, 30), key='-OUTPUT-', autoscroll=True, visible=False)]
]

layout = [
    [psg.Column(layoutOne, key='-QUOTE_COL-'), psg.Column(layoutTwo, key='-COMPANY_COL-', visible=False)],
]

window = psg.Window('Market Search', layout, size=(715, 500))

while True:
    event, values = window.read()
    if (event == 'Company_Pane'):
        window['-QUOTE_COL-'].update(visible=False)
        window['-COMPANY_COL-'].update(visible=True)
    if (event == 'Quotes_Pane'):
        window['-QUOTE_COL-'].update(visible=True)
        window['-COMPANY_COL-'].update(visible=False)
    if (event == 'Fetch_Quote' and values and '-SYMBOL-' in values and isinstance(values['-SYMBOL-'], str)):
        window['-QUOTE-'].update(value='', visible=False)
        symbol = values['-SYMBOL-']
        if symbol:
            quote_data = get_quote(symbol.upper())
            window['-QUOTE-'].update(value=quote_data, visible=True)
    if (event == 'Search_Company' and values and '-COMPANY-' in values and isinstance(values['-COMPANY-'], str)):
        window['-OUTPUT-'].update(value='', visible=False)
        symbol = values['-COMPANY-']
        if symbol:
            ai_response = ask(symbol.upper())
            window['-OUTPUT-'].update(value=ai_response, visible=True)
    if event in (None, 'Exit'):
        break

window.close()