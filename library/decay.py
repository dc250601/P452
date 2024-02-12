from . import random
import math


def Particle_Decay(Na,Nb,t0,tn,dt=2,tau_1=30):
    # Na = 500
    # Nb = 0
    # t0 = 0
    # tn = 120
    t = [t0]
    Na_hist =[Na]
    Nb_hist = [Nb]
    # dt = 2
    Number_steps = int((tn-t0)/dt)+1
    # tau_1 = 30 #To be inputted
    lamdba_1 = math.log(2)/tau_1
    rand = random.LGC(repeat=False)[-1]
    for i in range(Number_steps):
        for j in range(Na):
            rand = random.LGC(x0 = rand)[0]
            if rand<lamdba_1*dt:
                Na = Na-1
                Nb = Nb +1
        Na_hist.append(Na)
        Nb_hist.append(Nb)
        t.append(t[-1]+dt)
    return Na_hist,Nb_hist,t
