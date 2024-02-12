from . import linalg
from . import matrix
from . import linear

def sxx(x,y,dx):
    length = len(x)
    s = 0
    for i in range(length):
        s = s+(x[i]/dx[i])**2
    return s

def syy(x,y,dx):
    length = len(x)
    s = 0
    for i in range(length):
        s = s+(y[i]/dx[i])**2
    return s

def sxy(x,y,dx):
    length = len(x)
    s = 0
    for i in range(length):
        s = s + ((x[i]*y[i])/(dx[i]**2))
    return s


def sx(x,y,dx):
    length = len(x)
    s = 0
    for i in range(length):
        s = s + (x[i]/(dx[i]**2))
    return s


def s(x,y,dx):
    length = len(x)
    s = 0
    for i in range(length):
        s = s + 1/(dx[i]**2)
    return s


def sy(x,y,dx):
    length = len(x)
    s = 0
    for i in range(length):
        s = s + (y[i]/(dx[i]**2))
    return s


def linear_fit(x,y,dx=None):
    if dx is None:
        dx = linalg.init_list(len(x), mode = "constant", constant = 1)
    a1 = (sxx(x,y,dx)*sy(x,y,dx) - sx(x,y,dx)*sxy(x,y,dx))/(s(x,y,dx)*sxx(x,y,dx) - sx(x,y,dx)**2)
    a2 = (sxy(x,y,dx)*s(x,y,dx) - sx(x,y,dx)*sy(x,y,dx))/(s(x,y,dx)*sxx(x,y,dx) - sx(x,y,dx)**2)
    error_a1 = (sxx(x,y,dx)/(s(x,y,dx)*sxx(x,y,dx) - sx(x,y,dx)**2))**0.5
    error_a2 = (s(x,y,dx)/(s(x,y,dx)*sxx(x,y,dx) - sx(x,y,dx)**2))**0.5
    r2 = sxy(x,y,dx)**2/(sxx(x,y,dx)*syy(x,y,dx))
    return a1, a2, error_a1, error_a2, r2


def elem(x, k):
    s = 0
    for i in range(len(x)):
        s =s + x[i]**k
    return s


def elem_b(x,y,k):
    s = 0
    for i in range(len(x)):
        s =s + y[i]*(x[i]**k)
    return s


def poly_fit(x,y,order):
    """
    Function to find the matrix for polynomial fit.
    order: The number of terms to consider
    """
    mat = matrix.matrix_init(shape =(order+1,order+1), scheme="zero")
    b = linalg.init_list(order+1)
    for row in range(order+1):
        for col in range(order+1):
            mat.matrix[row][col] = elem(x,k=(row+col))
        b[row] = elem_b(x, y, k=row)
    _, coeff = linear.gauss_jordan(mat, b)
    return coeff
