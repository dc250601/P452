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
