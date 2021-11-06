#HW 6

import LA



"""Needs to normalize a vector
    Calculate the norm of the vector. Then multiply the vector by the
    reciprocal of the norm. Return the vector and the norm as a list
    Args:
        vector: the vector to be normalized
    Returns:
        A list, where the first element is the normalized vector and the
        second element is the norm of the original vector
"""
def normalize(vector: Vector) -> list[Vector, float]:
    norm: float = LA.pnorm(vector)
    result: Vector = LA.scalar_vec_multi(vector, 1/norm)
    return [result,norm]



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
def orthagonalize(vector: Vector, basis: Vector) -> list[Vector, complex]:
    factor: complex = LA.inpro(vector, basis)
    neg_proj: Vector = LA.scalar_vec_multi(basis, -1 * factor)
    result: Vector = LA.add_vectors(vector, neg_proj)
    return [result, factor]



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
def gram_schmidt(matrix: Matrix) -> list[Matrix, Matrix]:
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


"""Needs to give an orthogonal matrix with the span as the input matrix
    Performs modified gram-schmidt method for QR factorization and returns Q
    Args:
        matrix: The matrix to be orthonormalized, represented as a list of
          lists, where each component list represents a column vector
    Returns:
        An orthonormal matrix with the same span as the input matrix
"""
def orthonormalize(matrix: Matrix) -> Matrix:
    return gram_schmidt(matrix)[0]
