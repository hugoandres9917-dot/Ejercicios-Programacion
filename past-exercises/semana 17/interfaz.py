
#interfaz grafica de usuario para la gestion financiera personal
#con FreeSimpleGUI

import FreeSimpleGUI as sg
from data import load_data, save_data
from logica import FinanceManager

categories_data, movements_data = load_data()
manager = FinanceManager()

for cat in categories_data:
    manager.add_category(cat)
for mov in movements_data:
    title = mov.get("Titulo")
    amount = mov.get("Monto")
    category = mov.get("Categoria")
    is_income = mov.get("Tipo") == "Ingreso"
    payment_method = mov.get("Metodo de Pago", "Efectivo")
    notes = mov.get("Notas", "")
    manager.add_movement(
        title, amount, category, is_income,
        payment_method, notes
    )

#VENTANA PRINCIPAL CON TABLA DE MOVIMIENTOS 
layout = [
    [sg.Text("Gestor Financiero Personal", font=("Helvetica", 16))],
    [sg.Button("Agregar Categoría"), sg.Button("Agregar Movimiento"), sg.Button("Ver Balance")],
    [sg.Table(
        values=[m.to_row() for m in manager.movements],
        headings=["Titulo", "Monto", "Categoria", "Tipo", "Fecha", "Metodo de Pago", "Notas"],
        key="Tabla",
        auto_size_columns=True,
        display_row_numbers=False,
        justification="left",
        num_rows=10,
    )]
]


# Se crea ventana principal
window = sg.Window("Gestor Financiero Personal", layout)

# Bucle de eventos principal
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Salir"):
        #guardar datos al salir
        save_data(list(manager.categories.keys()), [m.__dict__ for m in manager.movements])
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
                success, message =manager.add_category(value_cat["nueva_categoria"])
                sg.popup("Resultado", message)
                break
            window_cat.close()

# Ventana para agregar un movimiento
    if event == "Agregar Movimiento":
        if not manager.categories:
            sg.popup("Alerta", "Debe agregar al menos una categoría antes de agregar movimientos.")
            continue

        layout_mov = [
            [sg.Text("Titulo:"), sg.InputText(key="Titulo")],
            [sg.Text("Monto:"), sg.InputText(key="Monto")],
            [sg.Text("Categoria"), sg.Combo(list(manager.categories.keys()), key="Categoria")],
            [sg.Text("Tipo"), sg.Radio("Ingreso", "Tipo", default=True, key="Ingreso"), 
            sg.Radio("Gasto", "Tipo", key="Gasto")],
            [sg.Button("Metodo de Pago:"), sg.Combo (["efectivo", "Tarjeta", "Transferencia"], key="metodo")],
            [sg.Text("Notas:"), sg.InputText(key="Notas")],
            [sg.Button("Guardar"), sg.Button("cancelar")],
        ]

        win_mov = sg.Window("Agregar Movimiento", layout_mov)
        while True:
            event_mov, value_mov = win_mov.read()
            if event_mov in (sg.WIN_CLOSED, "Cancelar"):
                break
            if event_mov == "Guardar":
                try:
                    amount = float(value_mov["Monto"])
                    is_income = value_mov["Ingreso"]
                    success, message = manager.add_movement(
                        value_mov["Titulo"], amount, value_mov["Categoria"], is_income,
                        value_mov.get("metodo", "Efectivo"), value_mov.get("Notas", "")
                    )
                    if success:
                        window["Tabla"].update(values=[m.to_row() for m in manager.movements])
                        save_data(list(manager.categories.keys()), [m.__dict__ for m in manager.movements])
                        sg.popup("Exito", message)
                        break
                    else:
                        sg.popup("Error", message)
                except KeyError:
                    sg.popup("Error", "Todos los campos son obligatorios")
                except ValueError:
                    sg.popup("Error", "El monto debe ser un numero valido")
        win_mov.close()

    if event == "Ver Balance":
        sg.popup("Balance", f"{manager.calculate_balance():,.2f}")
window.close()  