def bracketing(a, b, func, shift=1.5, max_iter=12):

    """
    Function to bracket for the bisection method

    args:
    a: The left hand side limit
    b: The right hand side limit
    func: The function on which bracketing is to be done
    shift: The amount to shift is bracketing is not satisfied
    max_iter: The number of iters to bracket till failure
    """

    for i in range(max_iter):
        if func(a)*func(b) < 0:
            return a, b
        else:
            if abs(func(a)) < abs(func(b)):
                a = a - shift*(b-a)
            if abs(func(a)) > abs(func(b)):
                b = b + shift*(b-a)
    print("Bracketing failed, use another guess, or increase the max_iter")


def bisection(a, b, func, eps=1e-6, delta=1e-6,shift=1.5, max_iter=12):
    """
    Function to find roots using the bisection method

    args:
    a: The left hand side limit
    b: The right hand side limit
    func: The function on which bracketing is to be done
    eps: The converge criterion measuring the difference between the bounds
    delta: The convergence criterion measuring the distance from zero or root
    shift: The amount to shift is bracketing is not satisfied
    max_iter: The number of iters to bracket till failure
    """
    if a < b:
        pass
    else:
        temp = a
        a = b
        b = temp
    hist  =[]

    if func(a)*func(b)<0:
        pass
    else:
        a,b = bracketing(a, b, func, shift, max_iter)
    
    if abs(b-a) < eps and abs(func(a)) < delta:
        print("Done, root found")
        return a,hist

    while(abs(b-a) > eps and abs(func(a)) > delta):
        c = (a+b)/2
        if func(c)*func(a)<0:
            b = c
        if func(c)*func(b)<0:
            a = c
        hist.append((a,b))

    return a,hist
