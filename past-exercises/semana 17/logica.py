
from datetime import datetime
import uuid


#organizar categorias en clase

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
    def __init__(self, title: str, amount: float, category: Category, is_income: bool, payment_method: str = "Efectivo", notes: str = ""):
        self.id = str(uuid.uuid4())[:8] 
        self.title = title.strip().title()
        self.amount = amount
        self.category = category
        self.type = "Ingreso" if is_income else "Gasto"
        self.payment_method = payment_method
        self.notes = notes
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_row(self):
        return [ 
            self.title,
            f"{self.amount:,.2f}",
            self.category,
            self.type,
            self.date.strftime("%Y-%m-%d %H:%M:%S"),
            self.payment_method,
            self.notes
        ]
    def __repr__(self):
        return f"Movimiento({self.title}, {self.amount}, {self.category.name}, {self.type}, {self.date})"

#clase gestor financiero

class FinanceManager:
    def __init__(self):
        self.categories = {}
        self.movements = []

    def add_category(self, name: str):
        if name.title() in self.categories:
            return False, "La categoria ya existe"
        try:
            category = Category(name)
            self.categories[category.name] = category
            return True, "Categoria agregada exitosamente"  
        except ValueError as e:
            return False, str(e)

    def add_movement(self, title: str, amount: float, category_name: str, is_income: bool, payment_method: str = "Efectivo", notes: str = ""):
        if category_name not in self.categories:
            return False, "Debe seleccionar una categoria valida"
        try:
            movement = Movement(title, amount, self.categories[category_name], is_income, payment_method, notes)
            self.movements.append(movement)
            return True, "Movimiento agregado exitosamente"
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