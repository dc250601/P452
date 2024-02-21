def newton_raphson(guess,func,func_p, eps):
    """
    guess: The initial guess to start the rooting from.
    func: The function whose root has to be found using the newton raphson method
    func_p: The first derivative of the function who root has to be found
    eps: The maximum error till which the code will run.
    """
    new_guess = 1e100
    while(True):
        new_guess = guess - func(guess)/func_p(guess)
        if abs(new_guess-guess)<eps:
            return new_guess
        guess = new_guess
