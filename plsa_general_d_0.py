import numpy as np
from numpy.random import rand
def ksum(A,dim):
    try:
        return np.sum(A,dim,keepdims=True)
    except:
        return np.expand_dims(np.sum(A,dim),dim)

def plsa(Nz,iteration,**kwargs):
    #dimension order Nz->Nd->Nw

    for p in kwargs:
        print p
        print kwargs[p]
    return
    Pa_z  = np.random.rand(Nz,Na, 1)
    Pb_z  = np.random.rand(Nz, 1,Nb)
    Pz    = np.random.rand(Nz, 1, 1)
    Pz_ab = np.random.rand(Nz,Na,Nb)

    for i in range(iteration):
        Pz_ab = Pa_z * Pb_z * Pz
        Pz_ab = Pz_ab/ksum(Pz_ab,0)
    
        Pzab = Nab*Pz_ab
        Pz   = ksum(ksum(Pzab,2),1)
        Pa_z = ksum(Pzab,2)/Pz
        Pb_z = ksum(Pzab,1)/Pz
        Pz   = Pz/ksum(Pz,0)
    return Pa_z, Pb_z


Nev={(0,1):rand(2,4), (1,2):rand(4,6), (2,0):rand(6,2)}
print Nev[(2,0)]
plsa(10,10,n0n1=rand(2,4),n1n2=rand(2,5),n2n0=rand(5,2))
