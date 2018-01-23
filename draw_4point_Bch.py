%matplotlib inline
#import sdf
import matplotlib
#matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from optparse import OptionParser
import os
from mpl_toolkits.mplot3d import Axes3D
import random
from mpl_toolkits import mplot3d
from matplotlib import rc
import matplotlib.mlab as mlab
rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

font = {'family' : 'Helvetic',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 16,
        }

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

enhance=np.loadtxt('./txt/enhance.txt')
axis_b=np.loadtxt('./txt/axis_b.txt')
axis_a=np.loadtxt('./txt/axis_a.txt')
ymax=np.loadtxt('./txt/ymax.txt')
bchf=np.loadtxt('./txt/bchf.txt')*10700


#T_phi=np.linspace(0.0,10.0,1000,endpoint=True)
#T_g=a0**2*np.cos(T_phi*2*np.pi+0.5*np.pi)**2/2.0+1.0
#plt.plot(T_phi,T_g,'-r',linewidth=2.5,label='theory')
#plt.scatter(x[index,which]/2/np.pi, y[index,which]/2/np.pi, c=rrt, s=500, cmap='rainbow', edgecolors='None')
#plt.plot(axis_b,bchf[:,0],'--b',linewidth=2.5,label=r'$a_0=$'+str(int(axis_a[0])))
#plt.plot(axis_b,bchf[:,1],'--r',linewidth=2.5,label=r'$a_0=$'+str(int(axis_a[1])))
#plt.plot(axis_b,bchf[:,2],'--k',linewidth=2.5,label=r'$a_0=$'+str(int(axis_a[2])))
#plt.plot(axis_b,bchf[:,3],'--g',linewidth=2.5,label=r'$a_0=$'+str(int(axis_a[3])))
plt.plot(axis_b,bchf[:,0],'ok',label=r'$a_0=$'+str(int(axis_a[0])))
plt.plot(axis_b,bchf[:,1],'^r',label=r'$a_0=$'+str(int(axis_a[1])))
plt.plot(axis_b,bchf[:,2],'xb',label=r'$a_0=$'+str(int(axis_a[2])))
plt.plot(axis_b,bchf[:,3],'+g',label=r'$a_0=$'+str(int(axis_a[3])))
x=np.linspace(0,30,500)
p0=100.0
y=2.0*(x*p0)**0.5*10700
plt.plot(x,y,'--c',linewidth=1.5,label=r'$\frac{B_{max}}{m_ec\omega/|e|}=2\sqrt{\alpha (p_0/m_ec)}$')
plt.legend(loc='upper right',framealpha=0.0)


#plt.colorbar()
#plt.xlim(47,53)
#plt.ylim(-1.1,-0.7)
plt.xlabel(r'$\alpha$',fontdict=font)
plt.ylabel(r'$B_{max}$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);

fig = plt.gcf()
fig.set_size_inches(8, 6)
#fig.savefig('./txt/Bmax_b.png',format='png',dpi=1280)
#plt.close("all")
#plt.show()