#%matplotlib inline
#import sdf
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from numpy import ma
from matplotlib import colors, ticker, cm
from matplotlib.mlab import bivariate_normal
from optparse import OptionParser
import os
#from colour import Color

######## Constant defined here ########
pi        =     3.1415926535897932384626
q0        =     1.602176565e-19 # C
m0        =     9.10938291e-31  # kg
v0        =     2.99792458e8    # m/s^2
kb        =     1.3806488e-23   # J/K
mu0       =     4.0e-7*pi       # N/A^2
epsilon0  =     8.8541878176203899e-12 # F/m
h_planck  =     6.62606957e-34  # J s
wavelength=     1.0e-6
frequency =     v0*2*pi/wavelength

exunit    =     m0*v0*frequency/q0
bxunit    =     m0*frequency/q0
denunit    =     frequency**2*epsilon0*m0/q0**2
#print 'electric field unit: '+str(exunit)
#print 'magnetic field unit: '+str(bxunit)
#print 'density unit nc: '+str(denunit)

font = {'family' : 'monospace',  
        'color'  : 'black',  
	    'weight' : 'normal',  
        'size'   : 20,  
       }  



ex=np.loadtxt('./txt/enhance.txt')
axis_b=np.loadtxt('./txt/axis_b.txt')
axis_a=np.loadtxt('./txt/axis_a.txt')
x,y=np.meshgrid(axis_b,axis_a)
#ex=ex.T*((y*100)**2/2.0+1)/(y**2/2.0+1)
levels = np.linspace(np.min(ex.T), np.max(ex.T), 40)
#plt.contourf(x, y, ex, levels=levels, cmap=cm.pink_r, antialiased=False)
#plt.pcolormesh(x, y, ex, norm=colors.SymLogNorm(linthresh=0.03, linscale=0.03, vmin=np.min(ex.T), vmax=np.max(ex.T)), cmap=cm.pink_r)
plt.pcolormesh(x, y, ex.T, cmap=cm.pink_r)

plt.axis([x.min(), x.max(), y.min(), y.max()])
#### manifesting colorbar, changing label and axis properties ####
cbar=plt.colorbar()#ticks=[np.min(ex), -eee/2, 0, eee/2, np.min()])
cbar.set_label('Enhanced ratio',fontdict=font)        

x=np.linspace(0.0005,0.1,200)
y0=0.5/(x)**0.5
y1=0.4/(x)**0.5
y2=0.3/(x)**0.5
y3=0.2/(x)**0.5
y4=0.1/(x)**0.5
plt.plot(x,y0,'--k',linewidth=0.5,label=r'$a_0*\sqrt{\alpha}=0.5$')
plt.plot(x,y1,'--r',linewidth=0.5,label=r'$a_0*\sqrt{\alpha}=0.4$')
plt.plot(x,y2,'--g',linewidth=0.5,label=r'$a_0*\sqrt{\alpha}=0.3$')
plt.plot(x,y3,'--b',linewidth=0.5,label=r'$a_0*\sqrt{\alpha}=0.2$')
plt.plot(x,y4,'--c',linewidth=0.5,label=r'$a_0*\sqrt{\alpha}=0.1$')
plt.legend(loc='upper right',framealpha=0.0)
plt.xlim(0.0,0.10)
plt.ylim(0.0,10.0)
plt.xlabel(r'$\alpha$',fontdict=font)
plt.ylabel(r'$a_0 [m_ec\omega/e]$',fontdict=font)
plt.xticks(fontsize=20); plt.yticks(fontsize=20);
plt.title(r'$\frac{\gamma_{max}}{\gamma_{vacuum}}$')
#plt.ylim(-1.1,-0.7)
#plt.title('electron at y='+str(round(y[n,0]/2/np.pi,4)),fontdict=font)


fig = plt.gcf()
fig.set_size_inches(8, 6)
#fig.set_size_inches(5, 4.5)
fig.savefig('./txt/enhance_b_a_t.png',format='png',dpi=1280)
plt.close("all")
