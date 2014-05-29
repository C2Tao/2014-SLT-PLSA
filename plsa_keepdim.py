import numpy as np

Ndw = np.random.rand(2,4)
Nz = 3
#dimension order Nz->Nd->Nw
[Nd,Nw] = np.shape(Ndw)
Pd_z  = np.random.rand(Nz,Nd, 1)
Pw_z  = np.random.rand(Nz, 1,Nw)
Pz    = np.random.rand(Nz, 1, 1)
Pz_dw = np.random.rand(Nz,Nd,Nw)
Pdw   = np.expand_dims(Ndw,2)

Pz_dw = Pd_z * Pw_z * Pz
Pz_dw = Pz_dw/np.sum(Pz_dw,0)

Pzdw = Ndw*Pz_dw
Pz   = np.sum(np.sum(Pzdw,2,keepdims=True),1,keepdims=True)
Pd_z = np.sum(Pzdw,2,keepdims=True)/Pz
Pw_z = np.sum(Pzdw,1,keepdims=True)/Pz

print np.shape(Pz),np.shape(Pd_z),np.shape(Pw_z)



#print np.shape(Pd_z),np.shape(Pw_z),np.shape(Pz)
#print Dz_dw
#print Sz_dw
#print Pz_dw

