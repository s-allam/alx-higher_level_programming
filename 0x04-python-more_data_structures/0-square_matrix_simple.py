#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple
def square_matrix_simple(mat):
    ans = [
        [x**2 for x in mat[0]],
        [x**2 for x in mat[1]],
        [x**2 for x in mat[2]],
    ]
    return ans 
