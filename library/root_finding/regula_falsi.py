from .bisection import bracketing
def regula(guess1, guess2, func,shift = 1.5, max_iter=12,eps = 1e-6):
    """
    regula: A function to find the roots of a function using regula falsi

    args:
    guess1: The first bound for the regula falsi
    guess2: The second bound for the regula falsi
    func: The function for which the roots is to be calculated
    """
    x0 = guess1
    x1 = guess2
    if func(guess1)*func(guess2)>0:
        x0,x1 = bracketing(guess1, guess2, func, shift=shift, max_iter=max_iter)
    else:
        pass
    hist = []
    counter =0
    while(True):
        counter = counter +1
        x = (x0*func(x1) - x1*func(x0))/(func(x1) - func(x0))
        if func(x1)*func(x)<0:
            x0 = x
        if func(x1)*func(x)>0:
            x1 = x
        hist.append((x0,x1))
        if (abs(func(x0) > eps)) and (abs(func(x1)) > eps):
            pass

        else:
               if abs(func(x0))<eps:
                   return x0,hist
               else:
                   return x1,hist
        if counter > 1000:
               print("Max iter reached")
