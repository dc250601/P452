from .. import matrix

def check_dominance(matrix, row_no):
    row = matrix.get_row(row_no)
    sum_ =0
    for i in range(len(row)):
        if i!=row_no:
            sum_ = sum_ +abs(row[i])
    if sum_<abs(row[row_no]):
        return True
    else:
        return False

    
def check_dominance_gen(matrix, row_no, col_no):
    row = matrix.get_row(row_no)
    sum_ =0
    for i in range(len(row)):
        if i!=col_no:
            sum_ = sum_ +abs(row[i])
    if sum_<abs(row[col_no]):
        return True
    else:
        return False
   

def make_dominant(matrix, row, B):
    for i in range(row+1, matrix.num_rows):
        if check_dominance_gen(matrix, i, row):
            temp = matrix.get_row(i)
            matrix.assign_row(i,matrix.get_row(row))
            matrix.assign_row(row, temp)
            temp = B.get_row(i)
            B.assign_row(i,B.get_row(row))
            B.assign_row(row, temp)
            
            return 0
    
    
def diag_dom(matrix, B):
    for row in range(matrix.num_rows):
        for col in range(matrix.num_cols):
            if row==col:
                if not check_dominance(matrix, row):
                    make_dominant(matrix, row, B)
                if check_dominance(matrix,row):
                    pass
            else:
                pass
            

def jacobi(A,B,x):
    x_new  = matrix.matrix_init(shape=(A.num_rows,1), scheme="zero")
    for i in range(x_new.num_rows):
        s = 0
        for j in range(x_new.num_rows):
            if j!=i:
                s = s + A.matrix[i][j]*x.matrix[j][0]
        x_new.matrix[i][0] = (1/A.matrix[i][i])*(B.matrix[i][0] - s)
    for row in range(B.num_rows):
        x.matrix[row][0] = x_new.matrix[row][0]
    return x

def mag(A,B):
    sum_ = 0
    for i in range(len(B)):
        sum_ = sum_ +abs(A[i]-B[i][0])
    sum_ = sum_
    return sum_


def gauss_jacobi(A,B,precision=1e-6):
    """
    gauss_jacobi: Function to solve a system of linear equations using gauss_jacobi iterative method
    args:
    args:
    A: A object of type matrix which is the matrix A of the equation
    B: A list which is the matrix B of the equation
    guess: The initial guess to start with
    precision: The precision upto which the loop should run, smaller the better
    Where the equation is AX = B
    """

    diag_dom(A,B)
    mag_=1e10
    iter_ =0
    guess = []
    for i in range(B.num_rows):
        temp = []
        temp.append(0)
        guess.append(temp)
    
    x = matrix.matrix(guess.copy())
    while(mag_>precision):
        iter_ = iter_ + 1
        initial = []
        for i in range(x.num_rows):
            initial.append(x.matrix[i][0])
        jacobi(A,B,x)
        mag_ = mag(initial,x.matrix)
        

        if iter_ > 100:
            print("Limit exceeded")
            break
    return x