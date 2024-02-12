
def deflate(a,root):
    deflated = a.copy()
    for i in range(1,len(a)):
        deflated[i] = root*deflated[i-1] +deflated[i]
    return deflated[:-1]


def derivative(a):
    der =[]
    for i in range(len(a)):
        der.append(a[i]*(len(a)-i-1))
    return der[:-1]


def root_check(a, root, eps):
    sum_ = 0
    for i in range(len(a)):
        sum_ = sum_ +a[i]*((root)**(len(a)-i-1))
    if abs(sum_) < eps:
        return True
    else:
        return False


def get_val(a, x):
    sum_ = 0
    for i in range(len(a)):
        sum_ = sum_ +a[i]*((x)**(len(a)-i-1))
    return sum_


def Laguerre(guess, a, eps=1e-5):
    """
    Laguerre: Function to find the roots of a polynomial using the Laguerre
    method

    args:
    guess: A guess value to start with.
    a: The cofficients of the polynomial in the descending order
    eps: The epsilon value or convergence criteriion

    For a polynomial of the form ax^3+bx^2+cx+d
    The a list will be [a,b,c,d]
    """
    roots = []
    beta = guess
    while(len(a) > 1):
        beta = guess
        while True:
            if root_check(a, beta, eps):
                roots.append(beta)
                a = deflate(a, beta).copy()
                break
            else:
                n = len(a)
                G = (get_val(derivative(a), beta))/(get_val(a,beta))
                H = G**2 - (get_val(derivative(derivative(a)), beta))/(get_val(a,beta))
                deno1 = (G+((n-1)*(n*H-G**2))**0.5)
                deno2 = (G-((n-1)*(n*H-G**2))**0.5)
                if abs(deno1)>abs(deno2):
                    deno = deno1
                else:
                    deno = deno2
                beta = beta - n/deno
    return roots
