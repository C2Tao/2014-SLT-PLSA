import numpy as np
from numpy.random import rand
def ksum(A,dim):
    try:
        return np.sum(A,dim,keepdims=True)
    except:
        return np.expand_dims(np.sum(A,dim),dim)

def plsa(Nz,iteration,Nnm,Nc):
    #dimension order Nz->Nd->Nwi
    nindex,nsize= [],[0 for i in range(Nc)]

    for i in range(Nc):
        for j in range(i+1,Nc):
            nindex += (i,j),
            x,y = np.shape(Nnm[(i,j)])
            nsize[i] = int(x)
            nsize[j] = int(y)
    print nindex,nsize


    Pnm={}
    for p in nindex:
        print p,Nc
        print np.shape(Nnm[p])
        for i in range(Nc-p[1]-1): 
            Nnm[p] = np.expand_dims(Nnm[p],2)
        print np.shape(Nnm[p])
        for i in range(p[1]-p[0]-1): 
            Nnm[p] = np.expand_dims(Nnm[p],1)
        print np.shape(Nnm[p])
        for i in range(p[0]): 
            Nnm[p] = np.expand_dims(Nnm[p],0)
        print np.shape(Nnm[p])
        Nnm[p] = np.expand_dims(Nnm[p],0)
        print np.shape(Nnm[p])
    #return


    ### Initialization ###
    Pn_z={}
    arg_order = [1] + np.ones(Nc).tolist()
    for n in range(Nc):
        args = arg_order[:]
        args[0]  = Nz
        args[n+1]= nsize[n]
        print args
        Pn_z[n] = rand(*args)
        print np.size(Pn_z[n])
    Pz = rand(*arg_order)
    Pz_nm = {}
    Pznm  = {}
    for p in nindex:
        args = arg_order[:]
        args[0] = Nz
        args[p[0]+1] = nsize[p[0]]
        args[p[1]+1] = nsize[p[1]]
        print args
        Pz_nm[p] = rand(*args) 
        Pznm[p]  = rand(*args) 
        print np.shape(Pz_nm[p])
    print "Initialized"


    for i in range(iteration):
        ### Expectation ###
        for p in nindex:
            Pz_nm[p] = Pn_z[p[0]] * Pn_z[p[1]] * Pz
            Pz_nm[p] = Pz_nm[p]/ksum(Pz_nm[p],0)
            Pznm[p] = Nnm[p] * Pz_nm[p]
        
        ### Maximization ###
        Pz = np.zeros(np.shape(Pz))
        for p in nindex:
            Pz = Pz + ksum(ksum(Pznm[p],p[0]+1),p[1]+1)
        Pz = Pz/ksum(Pz,0)
    
    
        print "beg"
        for p in nindex:
            print np.shape(Pznm[p])
            print np.shape(Pz_nm[p])
        print "end"


        for n in range(Nc):
            print np.shape(Pn_z[n])
            Pn_z[n] = np.zeros(np.shape(Pn_z[n]))
            for p in nindex:
                if   p[0]==n: 
                    print np.shape(Pn_z[n]),p,np.shape(Pn_z[n])
                    print np.shape(ksum(Pznm[p],p[1]+1))
                    Pn_z[n] += ksum(Pznm[p],p[1]+1)
                elif p[1]==n: 
                    print np.shape(Pn_z[n]),p,np.shape(Pn_z[n])
                    print np.shape(ksum(Pznm[p],p[0]+1))
                    Pn_z[n] += ksum(Pznm[p],p[0]+1)
            Pn_z[n] = Pn_z[n]/ksum(Pn_z[n],n+1)
        

    return
    '''
    Pa_z  = rand(Nz,Na, 1)
    Pb_z  = rand(Nz, 1,Nb)
    Pz    = rand(Nz, 1, 1)
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
    '''
Nev = {}
#Nev={(0,1):rand(2,4), (1,2):rand(4,6), (0,2):rand(2,6)}

nlist = [50,100,200,300]*3

for i in range(len(nlist)):
    for j in range(i+1,len(nlist)):
        Nev[(i,j)] = rand(nlist[i],nlist[j])


plsa(100,1,Nev,len(nlist))
