#%matplotlib inline
#%matplotlib inline
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from optparse import OptionParser
import os

font = {'family' : 'monospace',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 20,
        }
part_number=2500
nsteps=10001

insert='q250_'
t=np.loadtxt(insert+'t'+'.txt')
y=np.loadtxt(insert+'y'+'.txt')
x=np.loadtxt(insert+'x'+'.txt')
px=np.loadtxt(insert+'px'+'.txt')
py=np.loadtxt(insert+'py'+'.txt')
ey=np.loadtxt(insert+'e_part'+'.txt')
bz=np.loadtxt(insert+'b_part'+'.txt')
ay=np.loadtxt(insert+'a_part'+'.txt')
radn=np.loadtxt(insert+'radn'+'.txt')
radt=np.loadtxt(insert+'radt'+'.txt')

t=np.reshape(t,(part_number,nsteps))
x=np.reshape(x,(part_number,nsteps))
y=np.reshape(y,(part_number,nsteps))
px=np.reshape(px,(part_number,nsteps))
py=np.reshape(py,(part_number,nsteps))
ey=np.reshape(ey,(part_number,nsteps))
ay=np.reshape(ay,(part_number,nsteps))
radn=np.reshape(radn,(part_number,nsteps))
radt=np.reshape(radt,(part_number,nsteps))

gamma=np.sqrt(px**2+py**2+1)

plt.subplot(221)
plt.scatter(x[:,-1]/2/np.pi,y[:,-1]/2/np.pi,s=8,c=(192.0/255.0,0.0,0.0),label='RR',edgecolors='None')
plt.legend(loc='upper right')
plt.xlim(0.0,100.0)
plt.ylim(-50,50)
plt.xlabel('$x [\mu m]$',fontdict=font)
plt.ylabel('$y [\mu m]$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
plt.title('electron scatter distribution',fontdict=font)

plt.subplot(222)
plt.scatter(y[:,0]/2/np.pi,py[:,-1],s=8,c=(192.0/255.0,0.0,0.0),edgecolors='None')
plt.legend(loc='upper right')
plt.xlim(-2.5,2.5)
#plt.ylim(-50,50)
plt.xlabel('$y_0 [\mu m]$',fontdict=font)
plt.ylabel('$p_y [m_ec]$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
plt.title('p_y distribution',fontdict=font)

plt.subplot(223)
plt.scatter(y[:,0]/2/np.pi,radt[:,-1],s=8,c=(192.0/255.0,0.0,0.0),edgecolors='None')
plt.legend(loc='upper right')
plt.xlim(-2.5,2.5)
#plt.ylim(-50,50)
plt.xlabel('$y_0 [\mu m]$',fontdict=font)
plt.ylabel('$radt$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
plt.title('radiated total energy',fontdict=font)

plt.subplot(224)
plt.scatter(y[:,0]/2/np.pi,radn[:,-1],s=8,c=(192.0/255.0,0.0,0.0),edgecolors='None')
plt.legend(loc='upper right')
plt.xlim(-2.5,2.5)
#plt.ylim(-50,50)
plt.xlabel('$y_0 [\mu m]$',fontdict=font)
plt.ylabel('$radn$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
plt.title('radiated total number',fontdict=font)

fig = plt.gcf()
fig.set_size_inches(15, 15)
fig.savefig('./scatter.png',format='png',dpi=60)

