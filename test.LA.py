import pytest
import LA

def test_add_vectors():
    test_vector_01 = [1, 2, 3]
    test_vector_02 = [4, 5, 6]
    test_vector_03 = [1, 1, 2]
    assert LA.add_vectors(test_vector_01, test_vector_02) == [5, 7, 9]
    assert LA.add_vectors(test_vector_01, test_vector_03) == [2, 3, 5]


def test_scalar_vec_multi():
    vector_1 = [3, 2, 6]
    scalar_1 = 5
    vector_2 = [3, 4, 1]
    scalar_2 = 2
    assert LA.scalar_vec_multi(vector_1, scalar1_) == [15, 10, 30]
    assert LA.scalar_vec_multi(vector_2, scalar_2) == [6, 8, 2]


def test_scalar_matrix_multi():
    matrix_1 = [[1, 2, 3], [4, 5, 1], [1, 4, 2]]
    scalar_1 = 2
    matrix_2 = [[2, 4, 5], [8, 7, 3], [1, 2, 3]]
    scalar_2 = 4
    assert LA.scalar_matrix_multi(matrix_1, scalar_1) == [[2, 4, 6], [8, 10, 2], [2, 8, 4]]
    assert LA.scalar_matrix_multi(matrix_2, scalar_2) == [[8, 16, 20], [32, 28, 12], [4, 8, 12]]


def test_matrix_adding():
    matrix_1 = [[1, 1], [2, 2]]
    matrix_2 = [[3, 3], [4, 4]]
    matrix_3 = [[1, 0], [0, 1]]
    matrix_4 = [[3, 2], [1, 1]]
    assert LA.matrix_adding(matrix_1, matrix_2) == [[4, 4], [6, 6]]
    assert LA.matrix_adding(matrix_3, matrix_4) == [[4, 2], [1, 2]]


def test_matr_vec_multi():
    matrix_1 = [[3, 1], [3, 4]]
    vector_1 = [1, 1]
    matrix_2 = [[2, 2], [3, 3]]
    vector_2 = [2, 1]
    assert LA.matr_vec_multi(matrix_1, vector_1) == [6, 5]
    assert LA.matr_vec_multi(matrix_2, vector_2) == [7, 7]


def test_matr_matr_multi():
    matrix_1 = [[1, 3], [7, 8]]
    matrix_2 = [[3, 5], [4, 9]]
    matrix_3 = [[4, 4], [4, 6]]
    matrix_4 = [[2, 1], [5, 2]]
    assert LA.matr_matr_multi(matrix_1,matrix_2) == [[15,32],[53,107]]
    assert LA.matr_matr_multi(matrix_3,matrix_4) == [[28,12],[38,16]] 

    
    
#HW 4 test.LA Edits


def test_abs_value():
    assert LA.abs_value(4+3j) == 5
    assert LA.abs_value(-7j) == 7
    assert LA.abs_value(-8j-6) == 10


def test_pnorm_finite():
    assert LA.pnorm_finite([3, 4]) == 5
    assert LA.pnorm_finite([5, 12]) == 13


def test_infnorm():
    assert LA.infnorm([3, 4, 5, 7]) == 7
    assert LA.infnorm([3,0,4-5j]) == 6.4031242374328485


def test_p_norm():
    assert LA.p_norm([3, 4j+3]) == 5.830951894845301
    assert LA.p_norm([3, 4j+3],infinite = True) == 5


def test_inpro():
    assert LA.inpro(([1,2,3], [3,2,1])) == 10
    assert LA.inpro([complex(1, 8)], [complex(-3, 9)]) == (69+33j)

