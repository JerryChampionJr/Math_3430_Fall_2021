#HW8 Test Champion

import LS
import pytest



matrix1 = [[3,4,0],[-6,-8,1]]
vector1 = [-1,7,2]
matrix2 = [[3,4,7], [2,9,6], [1,5,3]]
vector2 = [1,4,2]

def test_least_squares():
    assert LS.least_squares(matrix1, vector1) == [(1+0j), (1.9999999999999991+0j)]
    assert LS.least_squares(matrix2, vector2) == [0.49999999999943157,-4.499999999994543,8.499999999989086]

