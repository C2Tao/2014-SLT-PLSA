import numpy as np
def ksum(A,dim):
    try:
        return np.sum(A,dim,keepdims=True)
    except:
        return np.expand_dims(np.sum(A,dim),dim)

def plsa(Nab,Nz,iteration):
    #dimension order Nz->Nd->Nw
    [Na,Nb] = np.shape(Nab)
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

print plsa(np.random.rand(100,100),3,100)
