import numpy as np
def ksum(A,dim):
    try:
        return np.sum(A,dim,keepdims=True)
    except:
        return np.expand_dims(np.sum(A,dim),dim)

def plsa(Nabc,Nz,iteration):
    #dimension order Nz->Nd->Nw
    shapes = np.shape(Nabc)
    [Na,Nb,Nc] = shapes 
    
    Pa_z  = np.random.rand(Nz,Na, 1, 1)
    Pb_z  = np.random.rand(Nz, 1,Nb, 1)
    Pc_z  = np.random.rand(Nz, 1, 1,Nc)
    Pz    = np.random.rand(Nz, 1, 1, 1)
    Pz_ab = np.random.rand(Nz,Na,Nb,Nc)

    for i in range(iteration):
        Pz_abc = Pa_z * Pb_z * Pc_z * Pz
        Pz_abc = Pz_abc/ksum(Pz_abc,0)
    
        Pzabc = Nabc*Pz_abc
        Pz   = ksum(ksum(ksum(Pzabc,1),2),3)
        Pa_z = ksum(ksum(Pzabc,2),3)/Pz
        Pb_z = ksum(ksum(Pzabc,1),3)/Pz
        Pc_z = ksum(ksum(Pzabc,1),2)/Pz
        Pz   = Pz/ksum(Pz,0)
    return Pa_z, Pb_z, Pc_z

print plsa(np.random.rand(10,10,10),3,100)
