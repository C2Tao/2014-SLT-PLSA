import numpy as np

Ndw = np.random.rand(2,4)
Nz = 3
#dimension order Nz->Nd->Nw
[Nd,Nw] = np.shape(Ndw)
Pd_z  = np.random.rand(Nz,Nd, 1)
Pw_z  = np.random.rand(Nz, 1,Nw)
Pz    = np.random.rand(Nz, 1, 1)
Pz_dw = np.random.rand(Nz,Nd,Nw)
Pdw   = Ndw[:,None]

Dz_dw = Pd_z * Pw_z * Pz
Sz_dw = np.sum(Dz_dw,0)
Pz_dw = Dz_dw/Sz_dw




print np.shape(Pd_z),np.shape(Pw_z),np.shape(Pz)
print Dz_dw
print Sz_dw
print Pz_dw

