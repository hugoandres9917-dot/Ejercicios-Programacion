#test_operations

import pytest
from operations import Operations

class TestOperations:
    def setup_method(self):
        self.op = Operations()
        
    def test_sum_positives(self):
        assert self.op.sum(5, 7) == 12
        
    def test_average_negatives(self):
        assert self.op.average([-2, -4, -6]) == -4
        
    def test_convert_zeros(self):
        assert self.op.convert_integer("0") == 0
        
        

