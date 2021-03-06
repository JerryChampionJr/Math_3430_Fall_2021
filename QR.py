#HW 6

import LA


def normalize(vector: Vector) -> list[Vector, float]:
    """Needs to normalize a vector
    Calculate the norm of the vector. Then multiply the vector by the
    reciprocal of the norm. Return the vector and the norm as a list
    Args:
        vector: the vector to be normalized
    Returns:
        A list, where the first element is the normalized vector and the
        second element is the norm of the original vector
    """
    norm: float = LA.pnorm(vector)
    result: Vector = LA.scalar_vec_multi(vector, 1/norm)
    return [result,norm]


def orthagonalize(vector: Vector, basis: Vector) -> list[Vector, complex]:
    """Calculate the vector rejection of vector on the basis
    Calculate the inner product between vector and basis. Use that
    inner product to calculate the negated vector projection of the vector on
    basis, then subtract that from vector. Return that vector rejection and the
    inner product used to calculate it.
    Args:
        vector: the vector to be orthagonalized
        basis: the vector to be orthagonalized against. Must be normalized.
    Returns:
        A list, where the first element is the orthagonalized vector, and the
        second element is the inner product of the vectors used to calculate it
    """
    factor: complex = LA.inpro(vector, basis)
    neg_proj: Vector = LA.scalar_vec_multi(basis, -1 * factor)
    result: Vector = LA.add_vectors(vector, neg_proj)
    return [result, factor]


def gram_schmidt(matrix: Matrix) -> list[Matrix, Matrix]:
    """Does modified gs method for QR factorization
    initialize q_matrix (Q) to be a copy of the input matrix and
    r_matrix (R) to be a zero matrix. Then, iterate
    every column vector in Q. Normalize the vector and store it in
    R then orthagonalize every following vector in Q
    relative to the current working column, storing this orthagonalization
    in R. Finally, return Q and R.
    Args:
        matrix: The matrix to be factored, represented as a list of list
          of column vectors
    Returns:
        A list of matrices, each represented as a list of lists, each component
        list representing a column vector. The first matrix is the orthonormal
        matrix Q and the second matrix is the upper triangular matrix R
    """
    q_matrix: Matrix = [column[:] for column in matrix]
    r_matrix: Matrix = [[0 for m in matrix] for n in matrix]

    for i, vector in enumerate(q_matrix):
        norm_operation = normalize(vector)
        q_matrix[i] = norm_operation[0]
        r_matrix[i][i] = norm_operation[1]
        for j, orth_vector in enumerate(q_matrix[i+1:], start=i+1):
            orth_operation = orthagonalize(orth_vector, vector)
            q_matrix[j] = orth_operation[0]
            r_matrix[j][i] = orth_operation[1]
    return [q_matrix, r_matrix]


#Problem 2

def orthonormalize(matrix: Matrix) -> Matrix:
    """Needs to give an orthogonal matrix with the span as the input matrix
    Performs modified gram-schmidt method for QR factorization and returns Q
    Args:
        matrix: The matrix to be orthonormalized, represented as a list of
          lists, where each component list represents a column vector
    Returns:
        An orthonormal matrix with the same span as the input matrix
    """
    return gram_schmidt(matrix)[0]


# HW7 Champion
# 11/15/2021
# QR Edits


#Problem 1:

def matconj(matrix: Matrix) -> Matrix:
    """Finds the conjugate transpose of a matrix
    Creates a matrix that is the conjugate transpose of the input matrix
    Args:
        matrix: A matrix, represented as a list of lists of complex numbers.
    Returns:
        The conjugate transpose of the matrix, represented in the same way.
    """
    d_m: int = len(matrix[0])  
    d_n: int = len(matrix)  
    result: Matrix = [[matrix[row][col].conjugate()
            for row in range(d_n)] for col in range(d_m)]
    return result


def outer_product(left_vector: Vector, right_vector: Vector) -> Matrix: 
    """Finds the outer product of two column vectors
    Calculate the conjugate transpose of right_vector and transform each
    vector into a matrix representation. Multiply these vector-matrices using
    the matrix multiply function, then return that matrix.
    Args:
        left_vector: a list of complex numbers
        right_vector: a list of complex numbers
    Returns:
        The outer product matrix = left_vector right_vector
    """
    right_vector_ct: Matrix = matconj([right_vector])
    left_vector_m: Matrix = [left_vector]
    result = LA.matr_matr_multi(left_vector_m, right_vector_ct)
    return result


def householder_qk(matrix_r: Matrix, k: int) -> Matrix:
    """Calculates q_k from the kth column of a matrix R for Householder QR
    Performs the mathematical algorithm to calculate q_k for Householder QR
    factorization.
    Args:
        matrix_r: (R), the original matrix from which q_k should be generated
        k: which column should be used as the base to generate q_k
    Returns:
        A matrix q_k such that q_k * matrix_r sets the kth column of matrix_r
        to be upper triangular
    """
    d_m = len(matrix_r[0])
    q_k: Matrix
    q_k = [[1 if i==j else 0 for i in range(d_m)] for j in range(d_m)]
    vec_x: Vector = matrix_r[k][k:]
    vec_v: Vector = q_k[k][k:]
    v_scl: float = LA.pnorm(vec_x) * (1 if vec_x[0].real >= 0 else -1)
    vec_v = LA.scalar_vec_multi(vec_v, v_scl)
    vec_v = LA.add_vectors(vec_v, vec_x)
    mat_f: Matrix = outer_product(vec_v, vec_v)
    f_scl: float = -2 / LA.inpro(vec_v, vec_v)
    mat_f = LA.scalar_matrix_multi(mat_f, f_scl)
    for i, f_col in enumerate(mat_f, start=k):
        q_k[i] = LA.add_vectors(q_k[i][:k] + f_col, q_k[i])
    return q_k


def householder(matrix: Matrix) -> list[Matrix, Matrix]:
    """Performs the householder method for QR factorization
    Initialize matrix_q (Q) as an identity matrix with the same number of rows
    as the input matrix, and matrix_r (R) as a copy of the input matrix. Then
    find successive matrices Q_k such that Q_k * R sets the kth column of R
    to be upper triangular. Update Q and R such that they are multiplied by
    Q_k, then once R is upper triangular, take the conjugate transpose of Q.
    Args:
        matrix: The matrix to be factored, represented as a list of lists of
          complex numbers
    Returns:
        A list of matrices, where the first element is the orthogonal matrix
        Q and the second element is the upper triangular matrix R
    """
    d_m: int = len(matrix[0])
    d_n: int = len(matrix)
    matrix_q: Matrix
    matrix_q = [[1 if i==j else 0 for i in range(d_m)] for j in range(d_m)]
    matrix_r: Matrix = [column[:] for column in matrix]
    for k, _ in enumerate(matrix_r):
        mat_q_k = householder_qk(matrix_r, k)
        matrix_r = LA.matr_matr_multi(mat_q_k, matrix_r)
        matrix_q = LA.matr_matr_multi(mat_q_k, matrix_q)
    matrix_q = matconj(matrix_q)
    return [matrix_q, matrix_r]

