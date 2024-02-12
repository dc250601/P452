from .. import matrix
from .. import linalg
import copy
# import math


def pivot(X, Y, order):

    def trigger(X, Y):
        column = X.get_column(order)[order+1:]
        swap_id = linalg.max_index(column) + order + 1
        # Swapping the rows of X
        matrix.swap_rows(X, order,swap_id)
        # Swapping in Y
        temp = Y[order]
        Y[order] = Y[swap_id]
        Y[swap_id] = temp

    if X.matrix[order][order] == 0:
        trigger(X, Y)


def unity(X, Y, column_no):
    size = len(X.matrix)
    val = X.matrix[column_no][column_no]
    for i in range(size):
        X.matrix[column_no][i] = X.matrix[column_no][i]/val
    Y[column_no] = Y[column_no]/val


def row_zero(X, Y, order):
    for row in range(X.num_rows):
        if row == order:
            pass
        else:
            multiple = X.matrix[row][order]
            for column in range(X.num_cols):
                X.matrix[row][column] = X.matrix[row][column] - multiple* X.matrix[order][column]
            Y[row] = Y[row] - multiple*Y[order]


def gauss_jordan(X, Y):
    """
    gauss_jordan: Function to solve a system of linear equations using Gauss Jordan
    elemination method.

    args:
    X: A object of type matrix which is the matrix A of the equation
    Y: A list which is the matrix B of the equation

    Where the equation is AX = B
    """
    size = len(Y)
    for i in range(size):
        pivot(X, Y, i)
        unity(X, Y, i)
        row_zero(X, Y, i)
    return X, Y


def inverter(X):
    """
    inverter:Function to invert a given matrix X
    
    args:
    X: A object of type matrix whose inverse is to be found
    """
    columns = X.num_cols
    rows = X.num_rows
    inv_X = matrix.matrix_init(shape =(rows,columns), scheme="zero")
    identity = matrix.matrix_init(shape=(rows,columns), scheme="identity")
    for i in range(columns):
        identity_column = identity.get_column(i)
        _,inverted_column = gauss_jordan(copy.deepcopy(X),identity_column)
        inv_X.assign_column(i,inverted_column)
    return inv_X