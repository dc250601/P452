import math
# import random
import sys
import os

from . import linalg
from . import random

class matrix:
    def __init__(self,matrix):
        assert len(matrix)>0, "Empty matrix recieved"
        self.num_rows = len(matrix)
        self.num_cols = len(matrix[0])
        self.matrix = matrix
        assert self.num_cols>0, "Fatal, matrix not of proper form"

    def get_row(self, row_no):
        temp = []
        for col in range(self.num_cols):
            temp.append(self.matrix[row_no][col])
        return temp

    def get_column(self, col_no):
        temp = []
        for row in range(self.num_rows):
            temp.append(self.matrix[row][col_no])
        return temp

    def get_diag(self):
        temp = []
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if row==col:
                    temp.append(self.matrix[row][col])
        return temp

    def assign_column(self, col_no, col):
        assert len(col)==self.num_rows, 'Incompartible sizes'
        for i in range(self.num_rows):
          self.matrix[i][col_no] = col[i]

    def assign_row(self, row_no, row):
        assert len(row)==self.num_cols, 'Incompartible sizes'
        for i in range(self.num_cols):
          self.matrix[row_no][i] = row[i]





    def __str__(self):
        _str=""
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.matrix[row][col]>=0:
                    pre = " "
                else:
                    pre = ""
                _str = _str+pre+str(self.matrix[row][col])+"\t"
            _str = _str+"\n"
        return _str



def matmul(A, B):
    """
    matmul: Function for multiplying two matrices A and B such the resultant is AB
    args:
    A: The first matrix of the object type matrix
    B: The second matrix of the object type matrix
    """
    def dot(l1,l2):
        sum_ = 0
        assert len(l1)==len(l2), "Shapes not matched"
        for i in range(len(l1)):
            sum_ = sum_ + l1[i]*l2[i]
        return sum_

    assert A.num_cols == B.num_rows, "Multiplication shape not matched for the matrices"
    new_matrix = matrix_init((A.num_rows,B.num_cols),scheme = "zero")
    for row in range(new_matrix.num_rows):
        for col in range(new_matrix.num_cols):
            elem = dot(A.get_row(row),B.get_column(col))
            new_matrix.matrix[row][col] = elem
    return new_matrix


def dot(l1,l2):
    """
    Function to calculate the dot product of two lists that are in matrix form
    """
    sum_ = 0
    assert l1.num_rows==l2.num_rows, "Shapes not matched"
    for i in range(l1.num_rows):
        sum_ = sum_ + l1.matrix[i][0]*l2.matrix[i][0]
    return sum_


def normalize_matrix_list(mat_list):
    """
    Function to return the normalised value of a list which is in matrix form
    """
    val = 0
    for i in range(mat_list.num_rows):
        val = val + mat_list.matrix[i][0]**2
    val = val**0.5
    for i in range(mat_list.num_rows):
        mat_list.matrix[i][0] = mat_list.matrix[i][0]/val
    

def matrix_init(shape, scheme):
    """
    matrix_init: Method to a matrix of given size with initialization as per given scheme

    args
    shape:Shape of the resultant matrix
    scheme: Initialization scheme

    """
    assert scheme in ("zero","LCG","identity"), f" This function currently does not support {scheme} init"
    rand = []
    if scheme is "LCG":
        rand =random.LGC(no_sample=shape[0]*shape[1]*5)
        rand =linalg.scale_list(rand)
    if scheme is "identity":
        z =[]
        for i in range(shape[0]):
            row =[]
            for j in range(shape[1]):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            z.append(row)
        return matrix(z)

    else:
        z =[]
        for i in range(shape[0]):
            row =[]
            for j in range(shape[1]):
                row.append(0)
            z.append(row)
        return matrix(z)

    z = []
    count =0
    for i in range(shape[0]):
        row =[]
        for j in range(shape[1]):
            while rand[count] == 0:
                count = count+1
            row.append(rand[count])
            count = count+1
        z.append(row)
    return matrix(z)

def swap_rows(A, id_1, id_2):

    """
    swap_rows: Method to swap the rows of a given matrix

    args
    A: The matrix whose rows will be swapped
    id_1: The first row number which will be swapped
    id_2: The second row number which will be swapped
    """
    row_1 = A.get_row(id_1)
    row_2 = A.get_row(id_2)
    A.assign_row(id_2, row_1)
    A.assign_row(id_1, row_2)
