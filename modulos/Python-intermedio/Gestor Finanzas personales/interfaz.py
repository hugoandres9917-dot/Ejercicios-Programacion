# interfaz grafica de usuario para la gestion financiera personal.

import FreeSimpleGUI as sg
from data import load_data, save_data
from logica import FinanceManager


def category(manager):
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
            success, message = manager.add_category(value_cat["nueva_categoria"])
            sg.popup("Resultado", message)
            if success:
                save_data(list(manager.categories.keys()), manager.movements)
            break
    window_cat.close()


def movement(manager, window, is_income=True):
    if not manager.categories:
        sg.popup("Alerta", "Debe agregar al menos una categoría antes de agregar movimientos.")
        return

    layout = [
        [sg.Text("Titulo:"), sg.InputText(key="Titulo")],
        [sg.Text("Monto:"), sg.InputText(key="Monto")],
        [sg.Text("Categoria"), sg.Combo(list(manager.categories.keys()), key="Categoria")],
        [sg.Text("Metodo de Pago:"), sg.Combo(["Efectivo", "Tarjeta", "Transferencia"], key="metodo")],
        [sg.Text("Notas:"), sg.InputText(key="Notas")],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]

    tipo = "Ingreso" if is_income else "Gasto"
    win = sg.Window(f"Agregar {tipo}", layout)

    while True:
        event, values = win.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        if event == "Guardar":
            try:
                amount = float(values["Monto"])
                success, message = manager.add_movement(
                    values["Titulo"], amount, values["Categoria"], is_income,
                    values.get("metodo", "Efectivo"), values.get("Notas", "")
                )
                if success:
                    window["Tabla"].update(values=[m.to_row() for m in manager.movements])
                    save_data(list(manager.categories.keys()), manager.movements)
                    sg.popup("Éxito", message)
                    break
                else:
                    sg.popup("Error", message)
            except ValueError:
                sg.popup("Error", "El monto debe ser un número válido")
    win.close()


def edit_movement(manager, window, movement_obj):
    layout = [
        [sg.Text("Titulo:"), sg.InputText(movement_obj.title, key="Titulo")],
        [sg.Text("Monto:"), sg.InputText(str(movement_obj.amount), key="Monto")],
        [sg.Text("Categoria"), sg.Combo(list(manager.categories.keys()), default_value=movement_obj.category.name, key="Categoria")],
        [sg.Text("Metodo de Pago:"), sg.Combo(["Efectivo", "Tarjeta", "Transferencia"], default_value=movement_obj.payment_method, key="metodo")],
        [sg.Text("Notas:"), sg.InputText(movement_obj.notes, key="Notas")],
        [sg.Button("Guardar"), sg.Button("Cancelar")]
    ]

    win = sg.Window("Actualizar Movimiento", layout)

    while True:
        event, values = win.read()
        if event in (sg.WIN_CLOSED, "Cancelar"):
            break
        if event == "Guardar":
            try:
                amount = float(values["Monto"])
                success, message = manager.update_movement_by_id(
                    movement_obj.id,
                    title=values["Titulo"],
                    amount=amount,
                    category=values["Categoria"],
                    is_income=(movement_obj.type == "Ingreso"),
                    payment_method=values.get("metodo", "Efectivo"),
                    notes=values.get("Notas", "")
                )
                if success:
                    window["Tabla"].update(values=[m.to_row() for m in manager.movements])
                    save_data(list(manager.categories.keys()), manager.movements)
                    sg.popup("Éxito", message)
                    break
                else:
                    sg.popup("Error", message)
            except ValueError:
                sg.popup("Error", "El monto debe ser un número válido")
    win.close()


def run_app():
    categories_data, movements_data = load_data()
    manager = FinanceManager()

    for cat in categories_data:
        manager.add_category(cat)

    for mov in movements_data:
        manager.movements.append(mov)

    layout = [
        [sg.Table(values=[m.to_row() for m in manager.movements],
                headings=["Titulo", "Monto", "Categoria", "Tipo", "Fecha", "Metodo de Pago", "Notas"],
                key="Tabla",
                auto_size_columns=True,
                display_row_numbers=False,
                justification="left",
                num_rows=10,
                enable_events=True,
                select_mode=sg.TABLE_SELECT_MODE_BROWSE)],
        [sg.Button("Agregar Categoría"), sg.Button("Agregar Gasto"), sg.Button("Agregar Ingreso"),
        sg.Button("Ver Balance"), sg.Button("Eliminar Movimiento"), sg.Button("Actualizar Movimiento"), sg.Button("Salir")]
    ]

    window = sg.Window("Gestor Financiero Personal", layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Salir"):
            save_data(list(manager.categories.keys()), manager.movements)
            break

        if event == "Agregar Categoría":
            category(manager)

        if event == "Agregar Gasto":
            movement(manager, window, is_income=False)

        if event == "Agregar Ingreso":
            movement(manager, window, is_income=True)

        if event == "Ver Balance":
            sg.popup("Balance", f"{manager.calculate_balance():,.2f}")

        if event == "Eliminar Movimiento":
            selected = values["Tabla"]
            if selected:
                index = selected[0]
                mov = manager.movements[index]
                success, message = manager.delete_movement_by_id(mov.id)
                if success:
                    window["Tabla"].update(values=[m.to_row() for m in manager.movements])
                    save_data(list(manager.categories.keys()), manager.movements)
                    sg.popup("Éxito", message)
                else:
                    sg.popup("Error", message)
            else:
                sg.popup("Error", "Debe seleccionar un movimiento para eliminar.")

        if event == "Actualizar Movimiento":
            selected = values["Tabla"]
            if selected:
                index = selected[0]
                mov = manager.movements[index]
                edit_movement(manager, window, mov)
            else:
                sg.popup("Error", "Debe seleccionar un movimiento para actualizar.")

    window.close()
