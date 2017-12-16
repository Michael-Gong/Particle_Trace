import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import colors, ticker, cm
font = {'family' : 'monospace',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 14,
        }

part_number=1200
nsteps=2
axis_a=np.linspace(210,450,21)
axis_w=np.linspace(30,110,21)
axis_g=np.linspace(500,2000,21)
axis_t=np.linspace(20,40,21)
rebo1=np.zeros([21,21])
rebo2=np.zeros([21,21])
rebo3=np.zeros([21,21])
rebo4=np.zeros([21,21])
rebo5=np.zeros([21,21])
rebo6=np.zeros([21,21])

ncore=24

def reform_shape(data):
    if len(data)%2==0:
        return np.reshape(data,(int(len(data)/nsteps),nsteps))
    else:
        return np.reshape(data[:-1],(int((len(data)-1)/nsteps),nsteps))

insert='3d_rr_aw/'
for ia in range(21):
    for iw in range(21):
        insert2='Dataa'+str(int(axis_a[ia]))+'w'+str(int(axis_w[iw]))+'/' 
        #t=np.loadtxt(insert+'t'+'.txt')
        #y=np.loadtxt(insert+'y'+'.txt')
        #x=np.loadtxt(insert+'x'+'.txt')
        px=np.array([]) #np.loadtxt(insert+insert2+'px_'+str(0)+'.txt')
        #py=np.loadtxt(insert+insert2+'py'+'.txt')
        #ey=np.loadtxt(insert+'e_part'+'.txt')
        #bz=np.loadtxt(insert+'b_part'+'.txt')
        #ay=np.loadtxt(insert+'a_part'+'.txt')
        for core in range(ncore):
            temp=np.loadtxt(insert+insert2+'px_'+str(core)+'.txt')
            px=np.concatenate((px,temp),axis=0)
        #t=np.reshape(t,(part_number,nsteps))
        #x=np.reshape(x,(part_number,nsteps))
        #y=np.reshape(y,(part_number,nsteps))
        px=reform_shape(px)
        #py=np.reshape(py,(part_number,nsteps))
        #py=np.reshape(py,(part_number,nsteps))
        #y=np.reshape(ey,(part_number,nsteps))
        #y=np.reshape(ay,(part_number,nsteps))
        #amma=np.sqrt(px**2+py**2+1)
        rebo1[ia,iw]=float(len(px[px[:,-1]>=0,-1]))/float(len(px[:,-1]))

plt.subplot(2,3,1) 
X,Y=np.meshgrid(axis_a,axis_w/10.)
Z=rebo1
#plt.imshow(rebo1,interpolation='none', cmap=cm.nipy_spectral)
levels = np.linspace(0.0, 1.0, 40)
plt.contourf(X, Y, Z.T, levels=levels, cmap=cm.nipy_spectral)
#### manifesting colorbar, changing label and axis properties ####
cbar=plt.colorbar(ticks=[0,0.5,1])
#cbar.set_label('Reflection ratio',fontdict=font)
plt.xlabel('$a_0$',fontdict=font)
plt.ylabel('$r_0 [\mu m]$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
#plt.title(name+' at '+str(round(time/1.0e-15,6))+' fs',fontdict=font)
#plt1 = plt.twinx()
#plt1.plot(x,ex[:,y.size/2.0],'-k',linewidth=2.5)       

insert='3d_rr_at/'
for ia in range(21):
    for it in range(21):
        insert2='Dataa'+str(int(axis_a[ia]))+'t'+str(int(axis_t[it]))+'/'  
        #t=np.loadtxt(insert+'t'+'.txt')
        #y=np.loadtxt(insert+'y'+'.txt')
        #x=np.loadtxt(insert+'x'+'.txt')
        px=np.array([]) #np.loadtxt(insert+insert2+'px'+'.txt')
        #py=np.loadtxt(insert+insert2+'py'+'.txt')
        #ey=np.loadtxt(insert+'e_part'+'.txt')
        #bz=np.loadtxt(insert+'b_part'+'.txt')
        #ay=np.loadtxt(insert+'a_part'+'.txt')
        for core in range(ncore):
            temp=np.loadtxt(insert+insert2+'px_'+str(core)+'.txt')
            px=np.concatenate((px,temp),axis=0)
        #t=np.reshape(t,(part_number,nsteps))
        #x=np.reshape(x,(part_number,nsteps))
        #y=np.reshape(y,(part_number,nsteps))
        px=reform_shape(px)
        #py=np.reshape(py,(part_number,nsteps))
        #y=np.reshape(ey,(part_number,nsteps))
        #y=np.reshape(ay,(part_number,nsteps))
        #amma=np.sqrt(px**2+py**2+1)
        rebo2[ia,it]=float(len(px[px[:,-1]>=0,-1]))/len(px[:,-1])

plt.subplot(2,3,2)        
X,Y=np.meshgrid(axis_a,axis_t/10.)
Z=rebo2
#plt.imshow(rebo1,interpolation='none', cmap=cm.nipy_spectral)
levels = np.linspace(0.0, 1.0, 40)
plt.contourf(X, Y, Z.T, levels=levels, cmap=cm.nipy_spectral)
#### manifesting colorbar, changing label and axis properties ####
cbar=plt.colorbar(ticks=[0,0.5,1])
#cbar.set_label('Reflection ratio',fontdict=font)
plt.xlabel('$a_0$',fontdict=font)
plt.ylabel(r'$\phi_\tau [2\pi]$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
#plt.title(name+' at '+str(round(time/1.0e-15,6))+' fs',fontdict=font)
#plt1 = plt.twinx()
#plt1.plot(x,ex[:,y.size/2.0],'-k',linewidth=2.5)    

insert='3d_rr_ag/'
for ia in range(21):
    for ig in range(21):
        insert2='Dataa'+str(int(axis_a[ia]))+'g'+str(int(axis_g[ig]))+'/'  
        #t=np.loadtxt(insert+'t'+'.txt')
        #y=np.loadtxt(insert+'y'+'.txt')
        #x=np.loadtxt(insert+'x'+'.txt')
        px=np.array([]) #np.loadtxt(insert+insert2+'px'+'.txt')
        #py=np.loadtxt(insert+insert2+'py'+'.txt')
        #ey=np.loadtxt(insert+'e_part'+'.txt')
        #bz=np.loadtxt(insert+'b_part'+'.txt')
        #ay=np.loadtxt(insert+'a_part'+'.txt')
        for core in range(ncore):
            temp=np.loadtxt(insert+insert2+'px_'+str(core)+'.txt')
            px=np.concatenate((px,temp),axis=0)
        #t=np.reshape(t,(part_number,nsteps))
        #x=np.reshape(x,(part_number,nsteps))
        #y=np.reshape(y,(part_number,nsteps))
        px=reform_shape(px)
        #py=np.reshape(py,(part_number,nsteps))
        #y=np.reshape(ey,(part_number,nsteps))
        #y=np.reshape(ay,(part_number,nsteps))
        #amma=np.sqrt(px**2+py**2+1)
        rebo3[ia,ig]=float(len(px[px[:,-1]>=0,-1]))/len(px[:,-1])
plt.subplot(2,3,3)        
X,Y=np.meshgrid(axis_a,axis_g)
Z=rebo3
#plt.imshow(rebo1,interpolation='none', cmap=cm.nipy_spectral)
levels = np.linspace(0.0, 1.0, 40)
plt.contourf(X, Y, Z.T, levels=levels, cmap=cm.nipy_spectral)
#### manifesting colorbar, changing label and axis properties ####
cbar=plt.colorbar(ticks=[0,0.5,1])
#cbar.set_label('Reflection ratio',fontdict=font)
plt.xlabel('$a_0$',fontdict=font)
plt.ylabel('$\gamma_0$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
#plt.title(name+' at '+str(round(time/1.0e-15,6))+' fs',fontdict=font)
#plt1 = plt.twinx()
#plt1.plot(x,ex[:,y.size/2.0],'-k',linewidth=2.5)      


insert='3d_qe_aw/'
for ia in range(21):
    for iw in range(21):
        insert2='Dataa'+str(int(axis_a[ia]))+'w'+str(int(axis_w[iw]))+'/'  
        #t=np.loadtxt(insert+'t'+'.txt')
        #y=np.loadtxt(insert+'y'+'.txt')
        #x=np.loadtxt(insert+'x'+'.txt')
        px=np.array([])#np.loadtxt(insert+insert2+'px'+'.txt')
        #py=np.loadtxt(insert+insert2+'py'+'.txt')
        #ey=np.loadtxt(insert+'e_part'+'.txt')
        #bz=np.loadtxt(insert+'b_part'+'.txt')
        #ay=np.loadtxt(insert+'a_part'+'.txt')
        for core in range(ncore):
            temp=np.loadtxt(insert+insert2+'px_'+str(core)+'.txt')
            px=np.concatenate((px,temp),axis=0)
        #t=np.reshape(t,(part_number,nsteps))
        #x=np.reshape(x,(part_number,nsteps))
        #y=np.reshape(y,(part_number,nsteps))
        px=reform_shape(px)
        #py=np.reshape(py,(part_number,nsteps))
        #y=np.reshape(ey,(part_number,nsteps))
        #y=np.reshape(ay,(part_number,nsteps))
        #amma=np.sqrt(px**2+py**2+1)

        rebo4[ia,iw]=float(len(px[px[:,-1]>=0,-1]))/len(px[:,-1])
plt.subplot(2,3,4) 
X,Y=np.meshgrid(axis_a,axis_w/10.)
Z=rebo4
#plt.imshow(rebo1,interpolation='none', cmap=cm.nipy_spectral)
levels = np.linspace(0.0, 1.0, 40)
plt.contourf(X, Y, Z.T, levels=levels, cmap=cm.nipy_spectral)
#### manifesting colorbar, changing label and axis properties ####
cbar=plt.colorbar(ticks=[0,0.5,1])
#cbar.set_label('Reflection ratio',fontdict=font)
plt.xlabel('$a_0$',fontdict=font)
plt.ylabel('$r_0 [\mu m]$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
#plt.title(name+' at '+str(round(time/1.0e-15,6))+' fs',fontdict=font)
#plt1 = plt.twinx()
#plt1.plot(x,ex[:,y.size/2.0],'-k',linewidth=2.5)       

insert='3d_qe_at/'
for ia in range(21):
    for it in range(21):
        insert2='Dataa'+str(int(axis_a[ia]))+'t'+str(int(axis_t[it]))+'/'  
        #t=np.loadtxt(insert+'t'+'.txt')
        #y=np.loadtxt(insert+'y'+'.txt')
        #x=np.loadtxt(insert+'x'+'.txt')
        px=np.array([])#np.loadtxt(insert+insert2+'px'+'.txt')
        #py=np.loadtxt(insert+insert2+'py'+'.txt')
        #ey=np.loadtxt(insert+'e_part'+'.txt')
        #bz=np.loadtxt(insert+'b_part'+'.txt')
        #ay=np.loadtxt(insert+'a_part'+'.txt')
        for core in range(ncore):
            temp=np.loadtxt(insert+insert2+'px_'+str(core)+'.txt')
            px=np.concatenate((px,temp),axis=0)

        #t=np.reshape(t,(part_number,nsteps))
        #x=np.reshape(x,(part_number,nsteps))
        #y=np.reshape(y,(part_number,nsteps))
        px=reform_shape(px)
        #py=np.reshape(py,(part_number,nsteps))
        #y=np.reshape(ey,(part_number,nsteps))
        #y=np.reshape(ay,(part_number,nsteps))
        #amma=np.sqrt(px**2+py**2+1)
        rebo5[ia,it]=float(len(px[px[:,-1]>=0,-1]))/len(px[:,-1])
plt.subplot(2,3,5)        
X,Y=np.meshgrid(axis_a,axis_t/10.)
Z=rebo5
#plt.imshow(rebo1,interpolation='none', cmap=cm.nipy_spectral)
levels = np.linspace(0.0, 1.0, 40)
plt.contourf(X, Y, Z.T, levels=levels, cmap=cm.nipy_spectral)
#### manifesting colorbar, changing label and axis properties ####
cbar=plt.colorbar(ticks=[0,0.5,1])
#cbar.set_label('Reflection ratio',fontdict=font)
plt.xlabel('$a_0$',fontdict=font)
plt.ylabel(r'$\phi_\tau [2\pi]$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
#plt.title(name+' at '+str(round(time/1.0e-15,6))+' fs',fontdict=font)
#plt1 = plt.twinx()
#plt1.plot(x,ex[:,y.size/2.0],'-k',linewidth=2.5)    

insert='3d_qe_ag/'
for ia in range(21):
    for ig in range(21):
        insert2='Dataa'+str(int(axis_a[ia]))+'g'+str(int(axis_g[ig]))+'/'  
        #t=np.loadtxt(insert+'t'+'.txt')
        #y=np.loadtxt(insert+'y'+'.txt')
        #x=np.loadtxt(insert+'x'+'.txt')
        px=np.array([])#np.loadtxt(insert+insert2+'px'+'.txt')
        #py=np.loadtxt(insert+insert2+'py'+'.txt')
        #ey=np.loadtxt(insert+'e_part'+'.txt')
        #bz=np.loadtxt(insert+'b_part'+'.txt')
        #ay=np.loadtxt(insert+'a_part'+'.txt')
        for core in range(ncore):
            temp=np.loadtxt(insert+insert2+'px_'+str(core)+'.txt')
            px=np.concatenate((px,temp),axis=0)

        #t=np.reshape(t,(part_number,nsteps))
        #x=np.reshape(x,(part_number,nsteps))
        #y=np.reshape(y,(part_number,nsteps))
        px=reform_shape(px)
        #py=np.reshape(py,(part_number,nsteps))
        #y=np.reshape(ey,(part_number,nsteps))
        #y=np.reshape(ay,(part_number,nsteps))
        #amma=np.sqrt(px**2+py**2+1)
        rebo6[ia,ig]=float(len(px[px[:,-1]>=0,-1]))/len(px[:,-1])
plt.subplot(2,3,6)        
X,Y=np.meshgrid(axis_a,axis_g)
Z=rebo6
#plt.imshow(rebo1,interpolation='none', cmap=cm.nipy_spectral)
levels = np.linspace(0.0, 1.0, 40)
plt.contourf(X, Y, Z.T, levels=levels, cmap=cm.nipy_spectral)
#### manifesting colorbar, changing label and axis properties ####
cbar=plt.colorbar(ticks=[0,0.5,1])
#cbar.set_label('Reflection ratio',fontdict=font)
plt.xlabel('$a_0$',fontdict=font)
plt.ylabel('$\gamma_0$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
#plt.title(name+' at '+str(round(time/1.0e-15,6))+' fs',fontdict=font)
#plt1 = plt.twinx()
#plt1.plot(x,ex[:,y.size/2.0],'-k',linewidth=2.5)       

#plt.figure(figsize=(100,100))
fig = plt.gcf()
fig.set_size_inches(38, 21)
fig.savefig('scan_3d_p.png',format='png',dpi=100)
plt.close("all")

