
#interfaz grafica de usuario para la gestion financiera personal
#con FreeSimpleGUI

import FreeSimpleGUI as sg
from data import load_data, save_data
from logica import add_category, validate_movement, create_movement, convert_movement_to_row

#Cargar datos iniciales
categories, movements = load_data()

#VENTANA PRINCIPAL CON TABLA DE MOVIMIENTOS 
layout = [
    [sg.Table(values=[[m["Monto"], m["Categoria"], m["Tipo"]] for m in movements],
                headings=["Monto", "Categoria", "Tipo"],
                key="tabla",
                auto_size_columns=True,
                justification="center",
                num_rows=10)],
    [sg.Button("Agregar Categoría"), sg.Button("Agregar Movimiento"), sg.Button("Salir")]
]
# Se crea ventana principal
window = sg.Window("Gestor Financiero Personal", layout)

# Bucle de eventos principal
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Salir":
        #guardar datos al salir
        save_data(categories, movements)
        break
# Ventana para agregar una categoria
    if event == "Agregar Categoría":
        layout_cat = [
            [sg.Text("Nombre de la categoría:")],
            [sg.InputText(key="nueva_categoria")],
            [sg.Button("Guardar"), sg.Button("Cancelar")]
        ]
        window_cat = sg.Window("Agregar Categoría", layout_cat)
        while True:
            event_cat, value_cat = window_cat.read()
            if event_cat in (sg.WIN_CLOSED, "Cancelar"):
                break
            if event_cat == "Guardar":
                new_name = value_cat["nueva_categoria"]
                success, message = add_category(categories, new_name)
                
                if success:
                    # Auto-guardar
                    save_data(categories, movements)
                    sg.popup("Éxito", message)
                else:
                    sg.popup("Error", message)
                break
        window_cat.close()

# Ventana para agregar un movimiento
    if event == "Agregar Movimiento":
        if not categories:
            sg.popup("Alerta", "Debe agregar al menos una categoría antes de agregar movimientos.")
            continue

        layout_mov = [
            [sg.Text("Monto:"), sg.InputText(key="Monto")],
            [sg.Text("Categoria:"), sg.Combo(categories, key="Categoria")],
            [sg.Text("Tipo"), sg.Radio("Ingreso", "Tipo", default=True, key="Ingreso"),
            sg.Radio("Gasto", "Tipo", key="Gasto")],
            [sg.Button("Guardar"), sg.Button("Cancelar")]
        ]
        win_mov = sg.Window("Agregar Movimiento", layout_mov)
        while True:
            event_mov, value_mov = win_mov.read()
            if event_mov in (sg.WIN_CLOSED, "Cancelar"):
                break
            if event_mov == "Guardar":
                amount_str = value_mov["Monto"]
                category = value_mov["Categoria"]
                is_income = value_mov["Ingreso"]
                
                valid, amount, cat, error = validate_movement(amount_str, category)
                
                if valid:
                    movement = create_movement(amount, cat, is_income)
                    movements.append(movement)
                    
                    # tabla actualizada
                    table_data = [[m["Monto"], m["Categoria"], m["Tipo"]] for m in movements]
                    window["tabla"].update(values=table_data)
                    
                    # guardar datos
                    save_data(categories, movements)
                    sg.popup("Éxito", "movimiento agregado exitosamente")
                    break
                else:
                    sg.popup("Error", error)
        win_mov.close()
window.close()

    


