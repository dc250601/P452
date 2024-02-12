def Lagrange_Interpolation(x,y,xp):
    """
    Lagrange_Interpolation: A function to interpolate using the method of Lagrange Interpolation
    
    arg:
    x: The list of data of x
    y: The list of data of f(x) or y
    xp: The value of x whose y is to be foud out
    """
    yp=0
    assert len(x)==len(y), "The length for the two arrays are different"
    for i in range(len(x)):
        p =1
        for j in range(len(y)):
            if i!=j:
                p = p*(xp-x[j])/(x[i]-x[j])
        yp = yp + p*y[i]
    return yp