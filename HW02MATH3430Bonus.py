# Jerry Champion Jr
# R11438744

"""
For this homework assignment we will take our work from HW01 and use it to
prepare a python script which will implement our algoirthms as python functions. 
For Problems #0-5 from HW01, Do the following.
1) Write your answer from HW01 in a comment.
2) Below the comment write a function which implements the algorithm from your
comment. If you find that you need to change your algorithm for your python
code, you must edit your answer in the comment. 
3) Test each of your functions on at least 2 inputs. 
4) Upload your .py file to a github repo named "Math_3430_Fall_2021"
This assignment is due by 11:59pm 09/27/2021. Do NOT upload an updated version to github
after that date. 
"""


#Example:

#Problem 00

"""
-The Three Questions
Q1: What do we have?
A1: Two vectors stored as lists. Denoted by the names vector_a and vector_b. 
Q2: What do we want?
A2: Their sum stored as a list.
Q3: How will we get there?
A3: We will create an empty list of the appropriate size and store the sums of
the corresponding components of vector_a and vector_b. 
-PsuedoCode
def add_vectors(vector_a,vector_b):
Initialize a result vector of 0's which is the same size as vector_a. Call this
vector result.
# Set each element of result to be equal to the desired sum.
for index in range(length(result)):
  result[index] = vector_a[index] + vector_b[index]
Return the desired result.
"""



def add_vectors(vector_a,vector_b):
  result = [0 for element in vector_a]
  for index in range(len(result)):
    result[index] = vector_a[index] + vector_b[index]
  return result



# Question 1

"""

Write an algorithm to implement scalar-vector multiplication.
Q1: What do we have?
A1: We have a scalar and a vector stored as a list.
Q2: What do we want?
A2: We want to have their final product stored as a new list.
Q3: How do we get there?
A3: We go through all the numbers in the vector[x] and multiply them by the scalar.
#Multiplies each element in "vector" by the "scalar".
def scalar_vector_multiplication(scalar, vector):
#Create empty list
result = []
#Go through all numbers in the vector and multiply them by scalar
for x in range(length(vector)):
	result[x] = vector[x] * scalar
#Return the result
return result

"""

def scalar_vector_multiplication(scalar, vector):
    result = [0 for element in vector]
    for x in range(len(vector)):
        result[x] = vector[x] * scalar
    return result



# Question 2

"""

Q1: What do we have?
A1: We have a scalar and a matrix stored in a list of lists.
Q2: What do we want?
A2: We want to have their final numbers stored as a new matrix.
Q3: How do we get there?
A3: We multiply each entry in the matrix by the scalar.
#Multiplies each element in "matrix" by the "scalar"
def scalar_matrix_multiplication(scalar, matrix):
create empty 2d list
result = [][]
#Go through all rows in the matrix
for row in range(length(matrix)):
#Go through all columns in row
	for column in range(length(matrix[row])):
		result[row][column] = matrix[row][column] * scalar
#Return the result
return result

"""



def scalar_matrix_multiplication(scalar, matrix):
    result = [[0 for element in range(len(matrix[0]))] for element in range(len(matrix))]
    for row in range(len(matrix)):
         for column in range(len(matrix[0])):
             result[row][column] = matrix[row][column] * scalar
    return result



# Question 3

"""

Q1: What do we have?
A1: We have two matrices, matrix_a and matrix_b stored as a list of lists.
Q2: What do we want?
A2: We want their final product to be stored in a new matrix.
Q3: How do we get there?
A3: We add each number in matrix_a with each number in matrix_b and place their final product in a new matrix.
#Adds each element in "matrix_a" with corresponding element in "matrix_b"
def matrix_addition(matrix_a, matrix_b):
#Create empty matrix
result[][]
#Go through each row in the matrix
for row in range(length(matrix_a)):
#Go through each column in row
	for column in range(length(matrix_a[row])):
#Add number in matrix_a with corresponding matrix_b number
		result[row][column] = matrix_a[row][column] + matrix_b[row][column]
#Return the result
return result

"""


def matrix_addition(matrix_a, matrix_b):
    result = [[0 for element in range(len(matrix_a[0]))] for element in range(len(matrix_a))]
    for row in range(len(matrix_a)):
        for column in range(len(matrix_a[row])):
             result[row][column] = matrix_a[row][column] + matrix_b[row][column]
    return result



# Question 4

"""

Q1: What do we have?
A1: We have a matrix with lists of numbers and a vector.
Q2: What do we want?
A2: We want to store their final product in a new matrix.
 
Q3: How will we get there?
A3: We multiply each number in the matrix to the corresponding number in the vector.
#Multiplies each number in matrix with corresponding number in vector
def matrix_vector_multiplication(matrix, vector)
Create empty matrix
result[][]
#Go through each row in matrix
for row in range(length(matrix)):
#Go through each column in matrix
	for column in range(length(matrix[row])):
#Multiply each number in matrix to corresponding number in vector
		result[row][column] = matrix[row][column] * vector[column]
#Return the result
return result

"""

def matrix_vector_multiplication(matrix, vector):
    result = [[0 for element in range(len(matrix[0]))] for element in range(len(matrix))]
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            result[row][column] = matrix[row][column] * vector[column]
    return result



# Question 5

"""

Q1: What do we have?
A1: We have two matrices represented as matrix_a and matrix_b.
Q2: What do we want?
A2: We want to create a new matrix with the final numbers of multiplying matrix_a to matrix_b.
Q3: How do we get there?
A3: We multiply each number in matrix_a with the corresponding number in matrix_b.
#Multiplies each number in matrix_a with corresponding number in matrix_b
def matrix_vector_multiplication(matrix_a, matrix_b)
Create empty matrix
result[][]
#Go through each row in matrix_a
for x in range(length(matrix_a)):
#Go through each column in matrix_b
	for y in range(length(matrix_b[x])):
#Go through each row in column in matrix_b
		for z in range(length(matrix_b)):
#Multiply each number in matrix_a to corresponding number in matrix_b
			result[x][y] = result[x][y] + matrix_a[x][z] * matrix_b[z][y]
#Return the result
return result

"""

def matrix_multiplication(matrix_a, matrix_b):
    result = [[0 for element in range(len(matrix_b[0]))] for element in range(len(matrix_a))]
    for x in range(len(matrix_a)):
    	for y in range(len(matrix_b[x])):
    		for z in range(len(matrix_b)):
    			result[x][y] = result[x][y] + matrix_a[x][z] * matrix_b[z][y]
    return result






test_vector_01 = [1, 2, 4]
test_vector_02 = [3, 1, 2]

# add_vectors(test_vector_01,test_vector_02) should output [4,3,6]
print('Test Output for add_vectors: ' + str(add_vectors(test_vector_01,test_vector_02)))
print('Should have been [4,3,6]')

print("\nTest #1")
print(scalar_vector_multiplication(2, [1, 2]))
print("\nTest #2")
print(scalar_matrix_multiplication(2, [[1, 2],[3, 4]]))
print("\nTest #3")
print(matrix_addition([[1, 2], [3, 4]],[[1, 2], [3, 4]]))
print("\nTest#4")
print(matrix_vector_multiplication([[1, 2], [3, 4]], [1, 2]))
print("\nTest #5")
print(matrix_multiplication([[1, 2, 3], [1, 2, 3]], [[1, 2],[1, 2], [1, 2]]))
