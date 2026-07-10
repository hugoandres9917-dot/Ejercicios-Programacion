# test_read_lines.py
import pytest
from archivo import read_lines
from unittest.mock import mock_open, patch

def test_read_lines_mock():
    contenido = "linea1\nlinea2\n"
    with patch("builtins.open", mock_open(read_data=contenido)):
        result = read_lines("fake_path.txt")
        assert result == ["linea1\n", "linea2\n"]

def test_read_lines_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_lines("no_existe.txt")
