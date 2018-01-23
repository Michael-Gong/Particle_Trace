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
bchf=np.loadtxt('./txt/bchf.txt')


#T_phi=np.linspace(0.0,10.0,1000,endpoint=True)
#T_g=a0**2*np.cos(T_phi*2*np.pi+0.5*np.pi)**2/2.0+1.0
#plt.plot(T_phi,T_g,'-r',linewidth=2.5,label='theory')
#plt.scatter(x[index,which]/2/np.pi, y[index,which]/2/np.pi, c=rrt, s=500, cmap='rainbow', edgecolors='None')
plt.plot(axis_b,ymax[:,0],'ok',label=r'$a_0=$'+str(int(axis_a[0])))
plt.plot(axis_b,ymax[:,1],'^r',label=r'$a_0=$'+str(int(axis_a[1])))
plt.plot(axis_b,ymax[:,2],'xb',label=r'$a_0=$'+str(int(axis_a[2])))
plt.plot(axis_b,ymax[:,3],'+g',label=r'$a_0=$'+str(int(axis_a[3])))
x=np.linspace(0.0001,0.04,400)
p0=10.0
y=(1/2.0/p0/x)**0.5/2/3.14159
plt.plot(x,y,'--c',linewidth=1.5,label=r'$\frac{y_{max}}{\lambda}=\sqrt{\frac{1}{2(p_0/m_ec)\alpha}}$')
plt.legend(loc='upper right',framealpha=0.0)

#plt.colorbar()
plt.xlim(-0.001,0.04)
#plt.ylim(0,3.9)
plt.xlabel(r'$\alpha$',fontdict=font)
plt.ylabel(r'$y_{max}/\lambda$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);

fig = plt.gcf()
fig.set_size_inches(8, 6)
#fig.savefig('./txt/y_b.png',format='png',dpi=1280)
#plt.close("all")
#plt.show()