import numpy as np
def ksum(A,dim):
    try:
        return np.sum(A,dim,keepdims=True)
    except:
        return np.expand_dims(np.sum(A,dim),dim)

def plsa(Ndw,Nz,iteration):
    #dimension order Nz->Nd->Nw
    [Nd,Nw] = np.shape(Ndw)
    Pd_z  = np.random.rand(Nz,Nd, 1)
    Pw_z  = np.random.rand(Nz, 1,Nw)
    Pz    = np.random.rand(Nz, 1, 1)
    Pz_dw = np.random.rand(Nz,Nd,Nw)
    Pdw   = np.expand_dims(Ndw,2)

    for i in range(iteration):
        Pz_dw = Pd_z * Pw_z * Pz
        Pz_dw = Pz_dw/ksum(Pz_dw,0)
    
        Pzdw = Ndw*Pz_dw
        Pz   = ksum(ksum(Pzdw,2),1)
        Pd_z = ksum(Pzdw,2)/Pz
        Pw_z = ksum(Pzdw,1)/Pz
        Pz   = Pz/ksum(Pz,0)
    return Pd_z, Pw_z 
