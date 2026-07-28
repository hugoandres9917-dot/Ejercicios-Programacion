#test_data.

import os
from data import save_data, load_data

def test_save_and_load_data(tmp_path):
    #arrange
    test_file = tmp_path / "test_finanzas.json"
    categories = ["Alimentacion", "Transporte"]
    movements = [{"Titulo": "Salario", "Monto": 1000, "Categoria": "Salario", "Tipo": "Ingreso"}]
    #act
    save_data(categories, movements)
    loaded_data = load_data()
    #assert
    assert categories == loaded_data[0]
    assert movements == loaded_data[1]
