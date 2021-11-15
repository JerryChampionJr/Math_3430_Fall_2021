import pytest
import QR

def test_gram_schmidt():
    assert QR.gram_schmidt([[1,0],[1,1]]) == [[[1,0],[0,1]],
                                                 [[1,0],[1,1]]]
    assert QR.gram_schmidt([[1,0],[-3,-3]]) == [[[1,0],[0,-1]],
                                                   [[1,0],[-3,3]]]


def test_orthonormalize():
    assert QR.orthonormalize([[1,0],[1,1]]) == [[1,0],[0,1]]
    assert QR.orthonormalize([[1,0],[-3,-3]]) == [[1,0],[0,-1]]

   
#HW 7 tests and adding equals_w_error to assist in testing

"""Tests if an item is equal to another within an error range
    Using recursion. If the arguments are iterable, compare each matching
    pair of elements in the arguments. Otherwise we have the base case, where
    we compare the absolute value of the difference between the each element
    with the margin of error. If false, we break recursion and return false,
    but if we get through all elements, we return true.
    Args:
        arg_a: A list or a complex number to be compared.
        arg_b: A list or a complex number to be compared. Must be the same
          type as arg_a and if a list, must be the same length as arg_a
        margin: A floating point number, the allowable error by which the
                absolute value of the args can differ
    Returns:
        A boolean value
"""
def equals_w_error(arg_a: list | complex, arg_b: list | complex, margin: float) -> bool:
    if hasattr(arg_a, '__iter__'):
        for var_a, var_b in zip(arg_a, arg_b):
            if not equals_with_error(var_a, var_b, margin):
                return False
    else:
        if abs(arg_a - arg_b) > margin:
            return False
    return True




def test_householder():
    expected_q1 = [[-.5, -.5, -.5, -.5], [.5, -.5, -.5, .5],
                   [-.5, .5, -.5, .5], [-.5, -.5, .5, .5]]
    expected_r1 = [[-2, 0, 0, 0], [-3, -5, 0, 0], [-2, 2, -4, 0]]
    expected_1 = [expected_q1, expected_r1]
    test_case_1 = [[1, 1, 1, 1], [-1, 4, 4, -1], [4, -2, 2, 0]]
    actual_1 = QR.householder(test_case_1)
    assert equals_w_error(actual_1, expected_1, MARGIN)
    expected_q2 = [[-2/3, -2/3, -1/3], [2/3, -1/3, -2/3], [-1/3, 2/3, -2/3]]
    expected_r2 = [[-3, 0, 0], [0, -3, 0], [-12, 12, -6]]
    expected_2 = [expected_q2, expected_r2]
    test_case_2 = [[2, 2, 1], [-2, 1, 2], [18, 0, 0]]
    actual_2 = QR.householder(test_case_2)
    assert equals_w_error(actual_2, expected_2, MARGIN)
