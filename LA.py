#Jerry Champion Jr
#HW 3

"""
For this assignment you will be writing a python script to be named LA.py. In
this script you will need to write 6 functions. Every function must 

1) Have a doc string.

2) Have type annotations

3) Be tested using unit testing. 

#0 A function which takes as it's arguments two vectors stored as
lists and returns their sum, also stored as a list.


#1 A function which takes as it's arguments a vector stored as a list and a
scalar, and returns the scalar vector multiplication stored as a list.


#2 A function which takes as it's arguments a matrix, stored as a list of lists
where each component list represents a column of the matrix(you cannot represent
the matrix as a list of rows!) and a scalar and returns their product, also
stored as a list of lists where each component list represents a column. You
must use the function from problem #1. Failure to use this function will result
in an earned grade of 0.

#3 A function which takes as it's arguments two matrices stored as lists of
lists where each component list represents a column vector, and returns their
sum stored in the same manner. You must use the function in problem #0 in your
method here. Failure to use the function from problem #0 will reuslt in an
earned grade of 0.

#4 A function which takes as it's argument a matrix (stored as a list of lists,
each component list representing a column vector), and a vector stored as a
list, and returns the matrix-vector product. This function must compute the
matrix-vector product by calculating the neccessary linear combination of the
input matrices columns. All other methods of matrix-vector multiplication are
strictly forbidden and their use will result in a grade of 0. For this function
you must use the functions written for problem #0 and problem #1. Failure to use
these functions will result in an earned grade of 0.

#5 A function which takes as it's arguments two matrices, each stored as a list
of lists where each component list represents a column vector, and returns their
product stored in the same manner. To earn any credit on this problem you must
use the function from problem #4 to implement the matrix-vector method of
matrix-matrix multiplication. Use of any other method will result in an earned
grade of 0.
"""

# Problem 0

def add_vectors(vector_a: list[float],
                vector_b: list[float]) -> list[float]:
    """Adds the two input vectors.

    Creates a result vector stored as a list of 0's the same length as the input 
    then overwrites each element of the result vector with the corresponding
    element of the sum of the input vectors. Achieves this using a for loop over
    the indices of result. 

    Args:
        vector_a: A vector stored as a list.
        vector_b: A vector, the same length as vector_a, stored as a list.

    Returns:
       The sum of the input vectors stored as a list. 
    """ 
    result: list[float] = [0 for element in vector_a]
    for index in range(len(result)):
        result[index] = vector_a[index] + vector_b[index]
    return result



# Problem 1:
""" Creates a result vector as an mpty list. The length of the result will return
    the same amount of elements in the vector. Then zeros are appended to the result list.
    Then it sets the result equal to the product of vector times the scalar.
    Achieved using a loop for the number of indices that are in the input vector.
    Arguments:
        vector_1: A vector stored as a list.
        scalar_1: A single value scalar.
    Returns:
        The product of the input vector and scalar stored as a list
"""
def scalar_vec_multi(vector_1: list[float], scalar_1: float) -> list[float]:
    result: list[float] = []
    for c in range(len(vector_1)):
        result[c] = result.append(0)

        result[c] = (vector_1[c] * scalar_1)
    return result


# Problem 2:
""" Override the initial indices of matrix_1 with the product of matrix_1 and
    the scalar. Use a for loop with the exact amount of indices that
    are in each row and column in the input matrix_1.The initial values for matrix_1
    are then overrode by the product.
    Arguments:
        matrix_1: A matrix stored as a list of multiple lists
        scalar_1: A single value scalar stored as a float integer
    Returns:
        The product of the input matrix and the scalar stored as list of lists.
"""

def scalar_matrix_multi(matrix_1: list[list[float]], scalar_1: float) -> list[list[float]]:
    for c in range(len(matrix_1)):
        matrix_1[c]= (scalar_vec_multi(matrix_1[c],scalar_1))
    return matrix_1


# Problem 3:
"""Override the initial indices of matrix_1 with the sum of matrix_1 and matrix_2.
    Done with a loop using the exact amount of indices that
    are in each column in the input matrix_1. The values for matrix_1
    are then overrode by the sum of botoh matrices with add_vectors.
    Arguments:
        matrix_1: A matrix stored as a list of lists
        matrix_2: A matrix stored as a list of lists
    Returns:
        The sum of both matrices stores as a list of lists.
"""
def matrix_adding(matrix_1: list[list[float]], matrix_2: list[list[float]]) -> list[list[float]]:

    for c in range(len(matrix_1)):
        matrix_1[c] = add_vectors(matrix_1[c], matrix_2[c])
    return matrix_1


#Problem 4:
"""Creates a result matrix stored as a list of lists. Zero's are then appended to the list
    for the same amount of indices in the matrix. Create a result vector stored as a
    list of zeros with the same amount of elements in the vector. Used in the previous function, scalar_vec_multi,
    we now use it to overwrite each column in matrix_1 with the product of the matrix_1 lists and vector_1 elements. Next step
    is to override the matrix_result by using the add_vectors function. Last override the vector_result with the last column in the matrix_result.Achieved using a for loop to compute add_vectors and
    scalar_vec_multi.
    Arguments:
        matrix_1: A matrix stored as a list of lists
        vector1_: A vector stored as a list
    Returns:
        The product of the the input vector and input matrix stored as a list
"""
def matr_vec_multi(matrix1: list[list[float]], vector1: list[float]) -> list[float]:
    matrix_result: list[list[float]] = [([0] * (len(matrix_1[0]))) for c in range(len(matrix_1))]
    vector_result: list[float] = []
    for c in range(len(vector_1)):
        vector_result[c] = vector_result.append(0)
        matrix_result[c] = scalar_vec_multi(matrix_1[c], vector_1[c])
    for c in range(len(matrix_result) - 1):
        matrix_result[c + 1] = add_vectors(matrix_result[c], matrix_result[(c + 1)])
    vector_result = matrix_result[len(matrix_result) - 1]
    return vector_result


#Problem 5:
"""Creates a matrix_result stored as a list of lists which contains zero's for same row length in matrix_1
    and same column length in matrix_2. Then overwrites all the columns in matrixresult with the corresponding product
    of matrix_1 and the columns in matrix_2.
    Argument:
        matrix_1: A matrix stored as a list of lists
        matrix_2: A matrix stored as a list of lists
    Returns:
        The product of the two input matrices stored as a list of lists
"""
def matr_matr_multi(matrix_1: list[list[float]], matrix_2: list[list[float]]) -> list[list[float]]:
    matrixresult: list[list[float]] = [([0] * (len(matrix_1[0]))) for c in range(len(matrix_2))]
    for c in range(len(matrix_2)):
        matrixresult[c] = matr_vec_multi(matrix_1, matrix_2[c])
    return matrixresult
