def newton_raphson(guess,func,func_p, eps):
    new_guess = 1e100
    while(True):
        new_guess = guess - func(guess)/func_p(guess)
        if abs(new_guess-guess)<eps:
            return new_guess
        guess = new_guess
