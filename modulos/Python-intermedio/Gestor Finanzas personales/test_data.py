#test_data.

import os
from data import save_data, load_data

def test_save_and_load_data(tmp_path):
    #arrange
    test_file = tmp_path / "test_finanzas.json"
    categories = ["Alimentacion"]
    movements = []
    #act
    save_data(categories, movements, file_path=str(test_file))
    loaded_categories, loaded_movements = load_data(file_path=str(test_file))
    #assert
    assert categories == loaded_categories
    assert movements == loaded_movements
