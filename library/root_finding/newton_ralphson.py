import numpy as np
def newton_raphson(guess,func,func_p, eps):
    """
    guess: The initial guess to start the rooting from.
    func: The function whose root has to be found using the newton raphson method
    func_p: The first derivative of the function who root has to be found
    eps: The maximum error till which the code will run.
    """
    new_guess = 1e100
    iter = 0
    while(True):
        iter = iter + 1
        new_guess = guess - func(guess)/func_p(guess)
        if abs(new_guess-guess)<eps:
            return new_guess, iter
        guess = new_guess
        

        
def newton_raphson_multivariable(F, J, x0, eps = 1e-4):
    """This function is used to find the root of a given function using Newton-Raphson method.
    
    Parameters:
    - F: The list containing all the functions of the system 
    - J: The Jacobian matrix of f of type library.matrix.
    - x0: The list of initial guess.
    - eps: The tolerance.
    
    """
    x = x0.copy()
    iter = 0
    while True:
        
        J_val = lib.matrix.matrix_init((2,2), scheme="zero")
        for row in range(J.num_rows):
            for col in range(J.num_cols):
                J_val.matrix[row][col] = J.matrix[row][col](x)
        
        F_val = lib.matrix.matrix(list([F[i](x)] for i in range(len(F))))
        J_val_inv = lib.matrix.matrix(np.linalg.inv(np.array(J_val.matrix)).tolist())
        x_p = lib.matrix.matmul(J_val_inv,F_val).get_column(0)
        x = list(x[i]-x_p[i] for i in range(len(x)))
        print(x)
        iter += 1
        if sum(list(abs(F[i](x)) for i in range(len(x)))) < eps:
            break
    return x, iter