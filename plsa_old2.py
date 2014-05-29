import numpy as np

Pdw = np.random.rand(2,4)
Nz = 3
[Nd,Nw] = np.shape(Pdw)
Pd_z = np.random.rand(Nd,Nz)
Pw_z = np.random.rand(Nw,Nz)
Pz = np.random.rand(Nz)
Pz_dw = np.random.rand(Nz,Nd,Nw)


#dimension order Nz->Nd->Nw
Pd_z = np.expand_dims(Pd_z.T,2) 
Pw_z = np.expand_dims(Pw_z.T,1) 
Pz = np.expand_dims(np.expand_dims(Pz,1),1)

print np.shape(Pd_z),np.shape(Pw_z),np.shape(Pz)
print Pd_z*Pw_z*Pz


