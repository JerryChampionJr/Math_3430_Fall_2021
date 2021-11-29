#HW 8 Champion
#LS

import LA
import QR

vec = list[complex]
mat = list[list[complex]]


def least_squares(matrix: mat, vector: vec) -> vec:
    """Finds the least squares solution of a matrix-vector product, Ax = b
    Starts by finding the QR factorization of the input matrix.  Solve the equation
    for Rx = Q*b, then perform back sub to find x, and return.
    Args:
        mat: The matrix A in the equation Ax = b
        vec: The vector b in the equation Ax = b
    Returns:
        The vecx in an equation formed Ax = b
    """
    vecx: vec = [None for _ in mat]
    mat_q: mat
    mat_r: mat
    mat_q, mat_r = QR.householder(mat)
    vec_v: vec = LA.matr_vec_multi(QR.matconj(mat_q), vec)
    for x_el in range(len(mat) - 1, 0 - 1, -1):
        con: complex = 0
        for i in range(x_el, len(vecx)):
            if i != x_el:
                con += vec_x[i] * mat_r[i][x_el]
        vecx[x_el] = (vec_v[x_el] - con) / mat_r[x_el][x_el]
    return vecx

