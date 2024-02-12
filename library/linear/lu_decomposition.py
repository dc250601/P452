from .. import matrix
from .. import linalg
import copy

def dolittle(X):
    for j in range(1,X.num_cols+1):
        for i in range(2,j+1):
            sum_ = 0
            for k in range(1,i):
                sum_ = sum_ + X.matrix[i-1][k-1]*X.matrix[k-1][j-1]
            X.matrix[i-1][j-1] = X.matrix[i-1][j-1] - sum_

        for i in range(j+1,X.num_cols+1):
            sum_ = 0
            for k in range(1,j):
                sum_ = sum_ + X.matrix[i-1][k-1]*X.matrix[k-1][j-1]
            X.matrix[i-1][j-1] = (X.matrix[i-1][j-1] - sum_)/(X.matrix[j-1][j-1])


def lu_solver(X, b):
    y = linalg.init_list(len(b))
    x = linalg.init_list(len(b))
    y[0] = b[0]
    dolittle(X)
    for i in range(2,X.num_cols+1):
        sum_ = 0
        for j in range(1,i):
            sum_ = sum_ + X.matrix[i-1][j-1]*y[j-1]
        y[i-1] = (b[i-1] - sum_)
    x[-1] = y[-1]/X.matrix[-1][-1]
    for i in range(X.num_cols-1, 0, -1):
        sum_ = 0
        for j in range(i+1, X.num_cols+1):
            sum_ = sum_ + X.matrix[i-1][j-1]*x[j-1]
        x[i-1] = ((1/X.matrix[i-1][i-1])*(y[i-1] - sum_))
    return x,y

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
        inverted_column,_ = lu_solver(copy.deepcopy(X),copy.deepcopy(identity_column))
        inv_X.assign_column(i,inverted_column)
    return inv_X