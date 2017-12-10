import sdf
import scipy.integrate as integrate
import scipy.special as special
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors, ticker, cm
%matplotlib inline  
font = {'family' : 'monospace',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 20,
        }


def E_B_field(x, y, z, t, a0, tau, r0):
    x=x/(2*np.pi)
    y=y/(2*np.pi)
    z=z/(2*np.pi)
    t=t/(2*np.pi)
    tau=tau/(2*np.pi)
    focus  =5.0
    delay  =10.0
    lambda0=1.0
    phase  =0.0
    polar  =1.0
################Gaussian beam#####################
    r2     = y**2+z**2
    z_R    = np.pi*r0**2/1.0
    w_z    = r0*(1.0+((x-focus)/z_R)**2)**0.5
    phi_G  = np.arctan((x-focus)/z_R)
    R_z    = (x-focus)*(1.0+(z_R/(x-focus))**2)
################Electric field####################    
    e_field_x = (1+polar)/2*a0*r0/w_z*y/z_R*np.exp(-((t-x-r2/(2.0*R_z))-delay)**2/tau**2)\
                *np.cos((t-x)*2*np.pi-2*np.pi*r2/(2.0*R_z)+phi_G+phase)\
                *np.exp(-r2/w_z**2)\
                +(1-polar)/2*a0*r0/w_z*z/z_R*np.exp(-((t-x-r2/(2.0*R_z))-delay)**2/tau**2)\
                *np.cos((t-x)*2*np.pi-2*np.pi*r2/(2.0*R_z)+phi_G+phase)\
                *np.exp(-r2/w_z**2)
    e_field_y = (1+polar)/2*a0*r0/w_z*np.exp(-((t-x-r2/(2.0*R_z))-delay)**2/tau**2)\
                *np.sin((t-x)*2*np.pi-2*np.pi*r2/(2.0*R_z)+phi_G+phase)\
                *np.exp(-r2/w_z**2)
    e_field_z = (1-polar)/2*a0*r0/w_z*np.exp(-((t-x-r2/(2.0*R_z))-delay)**2/tau**2)\
                *np.sin((t-x)*2*np.pi-2*np.pi*r2/(2.0*R_z)+phi_G+phase)\
                *np.exp(-r2/w_z**2)
################Magnetic field####################    
    b_field_x = (1+polar)/2*a0*r0/w_z*z/z_R*np.exp(-((t-x-r2/(2.0*R_z))-delay)**2/tau**2)\
                *np.cos((t-x)*2*np.pi-2*np.pi*r2/(2.0*R_z)+phi_G+phase)\
                *np.exp(-r2/w_z**2)\
                -(1-polar)/2*a0*r0/w_z*y/z_R*np.exp(-((t-x-r2/(2.0*R_z))-delay)**2/tau**2)\
                *np.cos((t-x)*2*np.pi-2*np.pi*r2/(2.0*R_z)+phi_G+phase)\
                *np.exp(-r2/w_z**2)
    b_field_y = -(1-polar)/2*a0*r0/w_z*np.exp(-((t-x-r2/(2.0*R_z))-delay)**2/tau**2)\
                *np.sin((t-x)*2*np.pi-2*np.pi*r2/(2.0*R_z)+phi_G+phase)\
                *np.exp(-r2/w_z**2)
    b_field_z = (1+polar)/2*a0*r0/w_z*np.exp(-((t-x-r2/(2.0*R_z))-delay)**2/tau**2)\
                *np.sin((t-x)*2*np.pi-2*np.pi*r2/(2.0*R_z)+phi_G+phase)\
                *np.exp(-r2/w_z**2)
    
    return e_field_x,e_field_y,e_field_z,b_field_x,b_field_y,b_field_z


def figureout(ex,x,y,name,t_0,n):
    print(np.max(ex),np.min(ex))
    if np.min(ex.T) == np.max(ex.T):
         return
    X, Y = np.meshgrid(grid_x/2/np.pi, grid_y/2/np.pi)
    eee=np.max([-np.min(ex.T),np.max(ex.T)])
    levels = np.linspace(-eee, eee, 40)
    plt.contourf(X, Y, ex.T, levels=levels, cmap=cm.RdBu)
    #### manifesting colorbar, changing label and axis properties ####
    cbar=plt.colorbar(ticks=[-eee, -eee/2, 0, eee/2, eee])
    cbar.set_label('Normalized electric field',fontdict=font)        
    plt.xlabel('X [$2\pi$]',fontdict=font)
    plt.ylabel('Y [$2\pi$]',fontdict=font)
    plt.xticks(fontsize=20); plt.yticks(fontsize=20);
    plt.title(r'The '+name+' at '+str(round(t_0/2/np.pi,3))+' $[2\pi]$',fontdict=font)
    #plt1 = plt.twinx()
    #plt1.plot(x,ex[:,y.size/2.0],'-k',linewidth=2.5)
    #plt1.set_ylabel('Normalized '+name)
    fig = plt.gcf()
    fig.set_size_inches(12, 7)
    fig.savefig('./laser_field/'+name+str(n).zfill(4)+'.png',format='png',dpi=100)
    plt.close("all")
    
def process(t_0,n):
    for ix in range(nx):
        for iy in range(ny):
            E_x[ix,iy],E_y[ix,iy],E_z[ix,iy],B_x[ix,iy],B_y[ix,iy],B_z[ix,iy]=\
            E_B_field(grid_x[ix],grid_y[iy],0.0,t_0,a_0,tau_0,r_0)
    figureout(E_x,grid_x,grid_y,'Ex',t_0,n)
    figureout(E_y,grid_x,grid_y,'Ey',t_0,n)
    figureout(E_z,grid_x,grid_y,'Ez',t_0,n)
    figureout(B_x,grid_x,grid_y,'Bx',t_0,n)
    figureout(B_y,grid_x,grid_y,'By',t_0,n)
    figureout(B_z,grid_x,grid_y,'Bz',t_0,n)

nx=200
ny=200
E_x=np.zeros([nx,ny])
E_y=np.zeros([nx,ny])
E_z=np.zeros([nx,ny])
B_x=np.zeros([nx,ny])
B_y=np.zeros([nx,ny])
B_z=np.zeros([nx,ny])
grid_x=np.linspace(0,20.01,nx)*2*np.pi
grid_y=(np.linspace(0,20.01,ny)-10.0)*2*np.pi
tau_0=5.0*2*np.pi
#t_0=30*2*np.pi
a_0=100.0
r_0=3.0
t_0=np.linspace(16.0,17.0,20)*2*np.pi
for it in range(20):
    process(t_0[it],it)