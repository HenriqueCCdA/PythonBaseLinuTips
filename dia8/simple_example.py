import PySimpleGUI as sg


sg.theme("Material1")


def soma(x:int, y:int) -> int:
    return x + y


# Widgets
layout = [
    [sg.Text("Number x"), sg.In(key="x", enable_events=True, size=(5, 1))],
    [sg.Text("Number y"), sg.In(key="y", enable_events=True, size=(5, 1))],
    [sg.Text("", key="result")],
    [sg.Button("Calcula")],
    [],
    [sg.Button("Sair")]
]


window = sg.Window(title="Calcula", layout=layout, margins=(100, 50))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Sair"):
        break
    if event == "Calcula":
        x = int(values["x"].strip())
        y = int(values["y"].strip())
        result = soma(x, y)
        window["result"].update(result)


window.close()
