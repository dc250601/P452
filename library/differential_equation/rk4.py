def runge_kutta(dxdt,dvdt,init_value, range_, h=0.01):
    """
    runge_kutta: Function to calculate the solution of a ODE by using the Runge Kutta method
    args:
    init_value: The starting values or x0, v0
    range_: The tuple corresponding to (t0,tn)
    h: The step size for each iteration
    """
    x = []
    v = []
    t = []

    k1x = []
    k2x = []
    k3x = []
    k4x = []

    k1v = []
    k2v = []
    k3v = []
    k4v = []

    x.append(init_value[0])
    v.append(init_value[1])
    t.append(range_[0])
    no_steps = int((range_[1]-range_[0])/h)
    for i in range(no_steps):
        k1x.append(h*dxdt(v[i],t[i]))
        k1v.append(h*dvdt(x[i],v[i],t[i]))

        k2x.append(h* dxdt((v[i]+k1v[i]/2),(t[i] + h/2)) )
        k2v.append(h* dvdt((x[i]+k1x[i]/2),v[i],(t[i] + h/2)) )

        k3x.append(h* dxdt((v[i]+k2v[i]/2),(t[i] + h/2)) )
        k3v.append(h* dvdt((x[i]+k2x[i]/2),v[i],(t[i] + h/2)) )

        k4x.append(h* dxdt((v[i]+k3v[i]),(t[i] + h)))
        k4v.append(h* dvdt((x[i]+k3x[i]),v[i],(t[i] + h)))

        x.append((x[i]+(k1x[i]+ 2*k2x[i] + 2*k3x[i] + k4x[i])/6))
        v.append((v[i]+(k1v[i]+ 2*k2v[i] + 2*k3v[i] + k4v[i])/6))
        t.append((t[i]+h))
    return x,v,t



def shooting_method(dxdt,dvdt,x0,xn,y0,yn,guessl):
    """
    shooting_method: Function to calculate the boundary value using shooting method
    """
    guessh = guessl
    guess = guessh
    Yh,Zh,Xh = runge_kutta(range_= (x0,xn), init_value=(y0,guess),dvdt=dvdt,dxdt=dxdt)
    if abs((Yh[-1] - yn)/yn) <= 0.001: # Tolerance value remove the hardwiring later
        return Yh,Zh,Xh
    while(True):
        Yh,Zh,Xh = runge_kutta(range_= (x0,xn), init_value=(y0,guessh),dvdt=dvdt,dxdt=dxdt)
        if Yh[-1]>yn:
            break
        guessh = guessh +2
    Yl,Zl,Xl = runge_kutta(range_= (x0,xn), init_value=(y0,guessl),dvdt=dvdt,dxdt=dxdt)
    if abs((Yl[-1] - yn)/yn) <= 0.001: # Tolerance value remove the hardwiring later
        return Yl,Zl,Xl
    guess =guessl
    while(True):
        Yl,Zl,Xl = runge_kutta(range_= (x0,xn), init_value=(y0,guess),dvdt=dvdt,dxdt=dxdt)
        if abs((Yl[-1] - yn)/yn) <= 0.001: # Tolerance value remove the hardwiring later
            return Yl,Zl,Xl 
        guess = guessl + ((guessh-guessl)/(Yh[-1] - Yl[-1]))*(yn-Yl[-1])
