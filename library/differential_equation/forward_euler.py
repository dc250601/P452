def forward_euler(func,step_size,x_0,y_0,x_n):
        X=[x_0]
        Y=[y_0]
        N=int(abs(x_0-x_n)/step_size)
        for i in range(N):
            x=X[-1]+step_size
            y=Y[-1]+step_size*func(X[-1],Y[-1])
            X.append(x)
            Y.append(y)
        return X,Y
