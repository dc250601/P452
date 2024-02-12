import math
from . import random
from . import linalg
def divide_the_initerval(a,b,N):
    """
    divide_the_initerval:
    Function to equally space the interval in N parts
    args:
    a: The first or lower bound of the interval
    b: The second or thed upper bound of the interval
    N: The number of intervals to divide into
    """
    temp = []
    h = (b-a)/N
    for i in range(N):
        temp.append((a+i*h,a+(i+1)*h))
    return temp


def integrate(func, N, a, b, mode = "midpoint"):
    """
    integrate:
    Function to integrate a given mathematical function using numerical analysis
    args;
    func: The fucntion which needs to be intgrated, type python standard funtion
    N: The number of intervals to divide into or integration
    a: The lower bound of integration
    b: The upper bound of integration
    mode: The mode of integration, available modes are midpoint, trapezoidal, simpson
    """
    h = (b-a)/N
    if mode == "midpoint":
        s = 0
        interval = divide_the_initerval(a,b,N)
        for i in range(len(interval)):
            s =s + h * func((interval[i][0]+interval[i][1])*0.5)
        return s
    if mode == "trapezoidal":
        s = 0
        interval = divide_the_initerval(a,b,N)
        for i in range(len(interval)):
            s = s + ( func(interval[i][0]) + func(interval[i][1]) )
        s = s*h*0.5
        return s
    if mode == "simpson":
        s = 0
        interval =divide_the_initerval(a,b,N)
        for i in range(len(interval)):
            s = s +  ( func(interval[i][0]) + func(interval[i][1]) )

        for i in range(len(interval)):
            if i%2 == 1 and i!=0:
                s = s + 2*func(interval[i][0])

        s = (s*h)/3
        return s


def monte_carlo_integration(N,limit,func):
    """
    monte_carlo_integration: A function to calculate the integral of a function using the Monte-Carlo
    integration method

    args:
    N(int): The number of smaples to take for integration
    limit(Tupe): A tuple of the form (a,b) where a is the lower and b is the upper limit
    func(Method Object): The function which needs to be integrated
    """

    a,b = limit
    x = random.LGC(no_sample=N)
    x = linalg.scale_list(x)
    x = list(map(lambda si: a + (b-a)*si,x))
    a_ = 0
    b_ = 0
    sum_ = 0
    for i in range(N):
        sum_ = sum_ + (b-a)*func(x[i])
        a_ += func(x[i])**2
        b_ = b_ + func(x[i])

    a_ = a_/N
    b_ = (b_/N)**2
    delta = (a_ - b_)
    sum_ = sum_/N
    return sum_,delta
