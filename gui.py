import FreeSimpleGUI as sg
import converter

label1 = sg.Text("Enter feet")
input1 = sg.InputText(tooltip="Enter feet", key="feet")
label2 = sg.Text("Enter inches")
input2 = sg.InputText(tooltip="Enter inches", key="inches")

convert_button = sg.Button("Convert", key="convert_values")

output_text = sg.Text("", key="output")

window = sg.Window("Metres to feet converter", layout=[[label1, input1],
                                                       [label2, input2],
                                                       [convert_button, output_text]])

while True:

    event, values = window.read()
    match event:
        case "convert_values":
            result = converter.convert(float(values['feet']), float(values['inches']))
            window["output"].update(value=f'{result} m', text_color="white")
        case sg.WIN_CLOSED:
            break

window.close()
