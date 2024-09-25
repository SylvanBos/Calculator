import PySimpleGUI as sg

sg.set_options(font=('Colibri 12'), button_element_size=(6,3))
button_size = (6, 3)
theme_menu = ['Menu',['LightGrey8', 'DarkGrey1', 'Dark', 'Random']]
start_getal = []
totaal_getal = []
def create_window(theme):
    sg.theme(theme)
    layout = [
        [sg.ButtonMenu("Theme's", menu_def=theme_menu, size=(6, 1), key='-MENU-')],
        [sg.Text('', expand_x=True), sg.Text("Output", key="-TEXT-", font='Colibri 20')],
        [sg.Button("Enter", key="-BUTTON_E-", expand_x=True), sg.Button("Clear", key="-BUTTON_C-", expand_x=True)],
        [sg.Button("7", size=button_size), sg.Button("8", size=button_size), sg.Button("9", size=button_size),
         sg.Button("/", size=button_size)],
        [sg.Button("4", size=button_size), sg.Button("5", size=button_size), sg.Button("6", size=button_size),
         sg.Button("*", size=button_size)],
        [sg.Button("1", size=button_size), sg.Button("2", size=button_size), sg.Button("3", size=button_size),
         sg.Button("-", size=button_size)],
        [sg.Button("0", key="-BUTTON_0-", expand_x=True), sg.Button(".", size=button_size),
         sg.Button("+", size=button_size)]
    ]

    return(sg.Window("Calculator", layout))


window = create_window('dark')


while True:
    event, values = window.Read()
    if event == sg.WIN_CLOSED:
        break

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        start_getal.append(event)
        num_string = ''.join(start_getal)
        window['-TEXT-'].update(num_string)

    if event in ['+','-','*','/']:
        totaal_getal.append(''.join(start_getal))
        start_getal = []
        totaal_getal.append(event)
        window['-TEXT-'].update('')


    if event == '-BUTTON_E-':
        totaal_getal.append(''.join(start_getal))
        antwoord = eval(''.join(totaal_getal))
        window['-TEXT-'].update(antwoord)
        start_getal = []
        totaal_getal = []

    if event == '-BUTTON_C-':
        window['-TEXT-'].update('')
        start_getal = []
        totaal_getal = []
        antwoord = ''
    theme = ''.join(values)
    if event == '-MENU-':
        window.close()
        window = create_window(theme)



window.close