from .. import linalg


def is_symmetric(X):
    flag = True
    for i in range(0,X.num_rows):
        for j in range(0,X.num_cols):
            if i != j:
                if X.matrix[i][j] != X.matrix[j][i]:
                    flag = False
    return flag

def cholesky(X):
    for i in range(X.num_rows):
        for j in range(X.num_cols):

            if i==j:
                sum_ = 0
                for k in range(i):
                    sum_ = sum_ + X.matrix[i][k]**2
                X.matrix[i][i] = (X.matrix[i][i] -sum_)**0.5
            elif i<j:
                sum_ = 0
                for k in range(i):
                    sum_ = sum_ + X.matrix[i][k]*X.matrix[k][j]
                X.matrix[i][j] = (X.matrix[i][j]-sum_)/(X.matrix[i][i])
                X.matrix[j][i] = X.matrix[i][j]

def cholesky_solver(X, b):
    y = linalg.init_list(len(b))
    x = linalg.init_list(len(b))
    if not is_symmetric(X):
        print("Non-Symmetric matrix cannot be solved by cholesky method")
        return 0

    cholesky(X)
    for i in range(0,X.num_cols,1):
        sum_ = 0
        for j in range(0,i):
            sum_ = sum_ + X.matrix[i][j]*y[j]
        y[i] = (b[i] - sum_)/(X.matrix[i][i])

    for i in range(X.num_cols-1, -1, -1):
        sum_ = 0
        for j in range(i+1, X.num_cols):
            sum_ = sum_ + X.matrix[i][j]*x[j]

        x[i] = (y[i] - sum_)/X.matrix[i][i]
    return x,y
