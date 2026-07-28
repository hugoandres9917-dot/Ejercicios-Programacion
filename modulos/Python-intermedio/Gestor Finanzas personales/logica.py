
import uuid
from datetime import date, datetime


#Clase para categorias.

class Category:
    def __init__(self, name: str):
        name = name.strip().title()
        if not name:
            raise ValueError("Debe ingresar un nombre válido")
        self.name = name

    def __repr__(self):
        return f"Category({self.name})"

#clase para movimientos financieros

class Movement:
    def __init__(self, title: str, amount: float, category: Category, is_income: bool, 
                payment_method: str = "Efectivo", notes: str = "", date=None):
        self.id = str(uuid.uuid4())[:8] 
        self.title = title.strip().title()
        self.amount = amount
        self.category = category
        self.type = "Ingreso" if is_income else "Gasto"
        self.payment_method = payment_method
        self.notes = notes

        if date is None:
            self.date = datetime.now()
        elif isinstance(date, str):
            try:
                self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                raise ValueError("La fecha debe tener el formato 'YYYY-MM-DD HH:MM:SS'")
        elif isinstance(date, datetime):
            self.date = date
        else:
            raise ValueError("La fecha debe ser un objeto datetime o una cadena con formato 'YYYY-MM-DD HH:MM:SS'")

    def to_row(self):
        return [ 
            self.title,
            f"{self.amount:,.2f}",
            self.category.name,
            self.type,
            self.date.strftime("%Y-%m-%d %H:%M:%S"),
            self.payment_method,
            self.notes
        ]
    def __repr__(self):
        return f"Movimiento({self.title}, {self.amount}, {self.category.name}, {self.type}, {self.date.strftime('%Y-%m-%d %H:%M:%S')}, {self.payment_method}, {self.notes})"

#clase gestor financiero

class FinanceManager:
    def __init__(self):
        self.categories = {}
        self.movements = []

    def add_category(self, name: str):
        if name.title() in self.categories:
            return False, f"La categoria '{name.title()}' ya existe"
        try:
            category = Category(name)
            self.categories[category.name] = category
            return True, f"Categoria '{category.name}' agregada exitosamente"  
        except ValueError as e:
            return False, str(e)

    def add_movement(self, title: str, amount: float, category_name: str, is_income: bool,
                        payment_method: str = "Efectivo", notes: str = "", date=None):
        if category_name not in self.categories:
            return False, "Debe seleccionar una categoria valida"
        if amount <= 0:
            return False, "El monto debe ser un número positivo."
        try:
            movement = Movement(title, amount, self.categories[category_name], is_income, payment_method, notes, date)
            self.movements.append(movement)
            return True, f"Movimiento '{movement.title}' agregado exitosamente"
        except ValueError as e:
            return False, str(e)

    def calculate_balance(self):
        ingresos = sum(m.amount for m in self.movements if m.type == "Ingreso")
        gastos = sum(m.amount for m in self.movements if m.type == "Gasto")
        return ingresos - gastos

    def movements_to_table(self):
        headers = ["Titulo", "Monto", "Categoria", "Tipo", "Fecha", "Metodo de Pago", "Notas"]
        rows = [m.to_row() for m in self.movements]
        return [headers] + rows