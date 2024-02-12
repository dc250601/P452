from .. import matrix


def seidel(A,B,guess):
    for i in range(A.num_rows):
        s = 0
        for j in range(A.num_cols):
            if j!=i:
                s = s+A.matrix[i][j]*guess.matrix[j][0]
        guess.matrix[i][0] = (B.matrix[i][0]-s)/A.matrix[i][i]


def mag(A,B):
    sum_ = 0
    for i in range(len(B)):
        sum_ = sum_ +abs(A[i]-B[i][0])
    sum_ = sum_
    return sum_


def gauss_seidel(A,B,G,precision = 1e-6):

    """
    gauss_seidel: Function to solve a system of linear equations using gauss_seidel iterative method
    args:
    args:
    A: A object of type matrix which is the matrix A of the equation
    B: A list which is the matrix B of the equation
    G: The initial guess to start with
    precision: The precision upto which the loop should run, smaller the better
    Where the equation is AX = B
    """

    mag_=1e10
    iter_ =0
    guess = []

    for i in range(B.num_rows):
        temp = []
        temp.append(G[i])
        guess.append(temp)

    x = matrix.matrix(guess.copy())
    while(mag_>precision):
        iter_ = iter_ + 1
        initial = []
        for i in range(x.num_rows):
            initial.append(x.matrix[i][0])
        seidel(A,B,x)
        mag_ = mag(initial,x.matrix)


        if iter_ > 100:
            print("Limit exceeded")
            break
    return x
