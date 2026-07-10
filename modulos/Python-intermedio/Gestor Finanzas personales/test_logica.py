#test_logica

import pytest
from logica import FinanceManager

def test_add_category_success():
    # Arrange
    manager = FinanceManager()
    # Act
    success, messsage = manager.add_category("Alimentacion")
    # Assert
    assert success == True
    assert messsage == "Categoria 'Alimentacion' agregada exitosamente"
    assert "Alimentacion" in manager.categories

def test_add_category_duplicate():
        # Arrange
        manager = FinanceManager()
        manager.add_category("Alimentacion")
        # Act
        success, message = manager.add_category("Alimentacion")
        # Assert
        assert success == False
        assert message == "La categoria 'Alimentacion' ya existe"

def test_add_movement_income():
    # Arrange
    manager = FinanceManager()
    manager.add_category("Salario")
    # Act
    success, message = manager.add_movement("Salario de junio", 1000, "Salario", True, "efectivo", "Pago mensual")
    #assert
    assert success == True
    assert message == "Movimiento 'Salario De Junio' agregado exitosamente"
    assert manager.movements[0].type == "Ingreso"
    assert manager.movements[0].amount == 1000

def test_balance_calculation():
    #arrange
    manager = FinanceManager()
    manager.add_category("Salario")
    manager.add_category("Alimentacion")
    manager.add_movement("Salario de junio", 1000, "Salario", True, "efectivo", "Pago mensual")
    manager.add_movement("Supermercado", 200, "Alimentacion", False, "efectivo", "Compra semanal")
    #act/assert
    assert manager.calculate_balance() == 800

def test_add_movement_without_category():
    #arrange
    manager = FinanceManager()
    #act
    success, message = manager.add_movement("Cena", 500, "Alimentacion", False)
    #assert
    assert success is False
    assert message == "Debe seleccionar una categoria valida"
    assert len(manager.movements) == 0

def test_add_movement_negative_amount():
    #arrange
    manager = FinanceManager()
    manager.add_category("Alimentacion")
    #act
    success, message = manager.add_movement("Cena", -500, "Alimentacion", False)
    #assert
    assert success is False
    assert message == "El monto debe ser un número positivo."
    assert len(manager.movements) == 0

    