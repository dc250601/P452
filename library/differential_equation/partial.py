def explicit(steps,init_func,init_t = (0,4), init_x = (0,2), nx = 20, nt = 5000):
    t = init_t
    x = init_x
    nx = nx
    nt = nt
    hx = (x[1]-x[0])/nx
    ht = (t[1]-t[0])/nt
    vx = []
    for i in range(nx+1):
        vx.append(init_func(i*hx+x[0]))
#     alpha = 0.72
    alpha = ht/(hx**2)
    for j in range(steps):
        vx_new = []
        for i in range(nx+1):
            if i==0:
                vx_new.append((1-2*alpha)*vx[0] + alpha*vx[1])
            if i==nx:
                vx_new.append((1-2*alpha)*vx[-1] + alpha*vx[-2])
            if i!=0 and i!=nx:
                vx_new.append((1-2*alpha)*vx[i] + alpha*vx[i-1] + alpha*vx[i+1])
        vx = vx_new.copy()
    x_ =[]
    for i in range(nx+1):
        x_.append(x[0]+i*hx)
    return x_,vx

def semi_implicit_euler(f,g, x0, v0, n, t_range):
    """
    The function to calculate the solution using semi-implicit Euler.
    """
    
    v = []
    x = []
    t0,tn = t_range
    
    dt = (tn-t0)/n
    
    v.append(v0)
    x.append(x0)
    t = 0
    for i in range(n):
        v.append(v[i] + g(t,x[i])*dt)
        x.append(x[i] + f(t,v[i+1])*dt)
        t = t+dt
    return x,v,t


def verlet(a, x0, v0, n, t_range):
    
    v = []
    x = []
    t0,tn = t_range
    dt = (tn-t0)/n
    
    x.append(x0)
    x.append(x0 + v0*dt + 0.5*a(x0)*(dt)**2)
    
    for i in range(n-1):
        x.append(2*x[-1] - x[-2] + a(x[-1])*(dt)**2)
    return x


def velocity_verlet(a, x0, v0, n, t_range):
    
    v = []
    x = []
    t0,tn = t_range
    dt = (tn-t0)/n
    
    x.append(x0)
    v.append(v0)
    
    for i in range(n):
        v_half_step = v[i] + 0.5*dt*a(x[i])
        x.append(x[i]+v_half_step*dt)
        v.append(v_half_step + 0.5*dt*a(x[i+1]))
    return x,v
    

def leapfrog(a,x0,v0,n,t_range):
    v = []
    x = []
    t0,tn = t_range
    dt = (tn-t0)/n
    
    x.append(x0)
    v.append(v0)
    
    for i in range(n):
        x.append(x[i]+v[i]*dt + 0.5*a(x[i])*(dt)**2)
        v.append(v[i] + 0.5*dt*(a(x[i+1])+a(x[i])))
    return x, v