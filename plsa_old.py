import numpy as np

Pdw = np.random.rand(2,4)
Nz = 3

[Nd,Nw] = np.shape(Pdw)
Pd_z = np.random.rand(Nd,Nz)
Pw_z = np.random.rand(Nw,Nz)
Pz = np.random.rand(Nz)
Pz_dw = np.random.rand(Nz,Nd,Nw)


#E step
print Pz_dw

for z in range(Nz):
    A = Pd_z[:,z].reshape(-1,1)
    B = Pw_z[:,z].reshape(1,-1)
    Pz_dw[z,:,:] = np.dot(A,B) * Pz[z]




A = np.expand_dims(Pd_z,2)
B = np.expand_dims(Pw_z.T,0)
print np.shape(A *B*Pz)
