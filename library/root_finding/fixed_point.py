def fixed_point_single_variable(g, guess, eps = 1e-4):
    """
    Function to find root using fixed point method for equation of a single variable

    args:
    g: The function g(x), such that g(x) = x
    guess: The guess values to start working with
    eps: The minimum error before the roots are returned
    """
    
    del_ = 1e5
    while(del_ > eps):
        guess_new = g(guess)
        del_ = abs(guess - guess_new)
        guess = guess_new
    return guess

def fixed_point_multi_variable(G, X, eps = 1e-4):
    """
    Function to find root using dixed point method for a system of equation
    
    args:
    G: list containing all the functions
    X: list containing initial guess values
    eps: The minimum error before the roots are returned
    """
    
    del_ = 1e5
    
    while del_ > eps:
        X_new = list(G[i](X) for i in range(len(X)))
        del_ = sum(list(abs(X_new[i] - X[i]) for i in range(len(X))))/len(X)
        X = X_new.copy()
    return X