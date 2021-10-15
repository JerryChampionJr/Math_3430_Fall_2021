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
