#ifndef _GIVEFIELD_H
#define _GIVEFIELD_H

#include <ctime>
#include <sys/timeb.h>
#include <math.h>
//#include <random>
#include "ovector.h"
#include "particle.h"
#include "common.h"

Vector3 A_field(Vector3 grid, Scalar time, Scalar a0, Scalar tau, Scalar r0)
{ Vector3 a_field;
  a_field.x1 = 0.0;
  a_field.x2 = a0*exp(-pow((time+grid.x1)-100*2*M_PI,2)/pow(tau*2*M_PI,2))*cos(time+grid.x1)*exp(-(pow(grid.x2,2)+pow(grid.x3,2))/pow(2*M_PI*r0,2));
  a_field.x3 = 0.0;
  return a_field;
};

Vector3 E_field(Vector3 grid, Scalar time, Scalar a0, Scalar tau, Scalar r0)
{ Vector3 e_field;
  e_field.x1 = 0.0;
  e_field.x2 = a0*exp(-pow((time+grid.x1)-100*2*M_PI,2)/pow(tau*2*M_PI,2))*sin(time+grid.x1)*exp(-(pow(grid.x2,2)+pow(grid.x3,2))/pow(2*M_PI*r0,2));
  e_field.x3 = 0.0;
  return e_field;
};

Vector3 B_field(Vector3 grid, Scalar time, Scalar a0, Scalar tau, Scalar r0)
{ Vector3 b_field;
  b_field.x1 = 0.0;
  b_field.x2 = 0.0;
  b_field.x3 = -a0*exp(-pow((time+grid.x1)-100*2*M_PI,2)/pow(tau*2*M_PI,2))*sin(time+grid.x1)*exp(-(pow(grid.x2,2)+pow(grid.x3,2))/pow(2*M_PI*r0,2));
  return b_field;
};

Scalar factor(Vector3 data)
{ Scalar result;
  result = sqrt(1.0+data*data);
  return result;
};

Vector3 velocity(Vector3 data)
{ Vector3 v;
  v = data/factor(data);
  return v;
};

Scalar get_time()
{ timeb tm;
  ftime(&tm);
  return tm.time+0.001*tm.millitm;
};

#ifdef QED_BLOCK
Scalar initial_optical_depth()
{ 
  Scalar depth, p_tau;
  p_tau = (rand()/(double)RAND_MAX);  
  depth = -log(1.0-p_tau);
  return depth;
}

Scalar calculate_eta(Particle p)
{ 
  Scalar E_s = 4.12e5;
  Scalar eta;
  Vector3 e_p;
  e_p = (p.e_part-p.uu*p.e_part/p.uu.magnitude()+p.uu.cross(p.b_part)/p.gamma)*p.gamma;
  eta =  e_p.magnitude()/E_s;
  return eta;  
}

Scalar find_value_from_table_1d(Scalar x_in, int h_sample, Scalar x[], Scalar values[])
{ 
  Scalar value;  
  Scalar fx, x_value, value_interp, xdif1, xdif2, xdifm;
  int i1, i2, im;
  static bool warning = true;

  x_value = log10(x_in);
  i1 = 0;
  i2 = h_sample-1;
  xdif1 = x[i1] - x_value;
  xdif2 = x[i2] - x_value;
  if (xdif1 * xdif2 < 0)
  {
      // Use bisection to find the nearest cell
      do
      {
        im = (i1 + i2) / 2;
        xdifm = x[im] - x_value;
        if (xdif1 * xdifm < 0) 
          { 
	    i2 = im;
          }
        else
          {
	    i1 = im;
            xdif1 = xdifm;
          }
      }while((i2-i1)!=1);
      // Interpolate in x
      fx = (x_value - x[i1]) / (x[i2] - x[i1]);
  }
  else
  {
      if (warning == true)
      {
        fprintf(stderr, "*** WARNING ***\nArgument to find_value_from_table_1d outside the range of the table.\nUsing truncated value. No more warnings will be issued.\n");
        warning = false;
      }
      if (xdif1 >= 0)
        {fx = 0.0 ;}
      else
        {fx = 1.0 ;}
  }
    value_interp = (1.0 - fx)*values[i1]+fx*values[i2];
    value = pow(10.0,value_interp);
    return value;
}

Scalar delta_optical_depth(Scalar eta, Scalar gamma, int h_sample, Scalar T1_1[], Scalar T1_2[])
{
  Scalar delta, hsokolov, tau_c;
  hsokolov = find_value_from_table_1d(eta,h_sample,T1_1,T1_2);
  tau_c = 1.05e-34/(0.51*1.6e-13);
  delta = dt/2.0/M_PI*3.3333e-15*eta/137.0*sqrt(3.0)*hsokolov/(2*M_PI*tau_c*gamma);
  return delta;
}

Scalar find_value_from_table_alt(Scalar x_in, Scalar p_value, int nx, int ny, Scalar x[], Scalar y[][100], Scalar T2[][100])
{
  Scalar value;
  int ix, index_lt, index_gt, i1, i2, im;
  Scalar fx, fp, y_lt, y_gt, x_value, y_interp, xdif1, xdif2, xdifm;
  static bool warning = true;
  x_value = log10(x_in);
  // Scan through x to find correct row of table
  i1 = 0;
  i2 = nx-1;
  xdif1 = x[i1] - x_value;
  xdif2 = x[i2] - x_value;
  if (xdif1 * xdif2 < 0)
    {  // Use bisection to find the nearest cell
      do
       {
        im = (i1 + i2) / 2;
        xdifm = x[im] - x_value;
        if (xdif1 * xdifm < 0)
          {i2 = im;}
        else
          {
           i1 = im;
           xdif1 = xdifm;
          }
       }while((i2-i1)!=1);
      // Interpolate in x
      fx = (x_value - x[i1]) / (x[i2] - x[i1]);
   }
   else
   {
      if (warning) 
       {
        fprintf(stderr,"*** WARNING ***\n Argument to find_value_from_table_alt outside the range of the table.\nUsing truncated value. No more warnings will be issued.");
        warning = false;
       }
      if (xdif1 >= 0)
        {fx = 0.0 ;}
      else
        {fx = 1.0 ;}
   }

    index_lt = i1;
    index_gt = i2;

    ix = index_lt;
    // Scan through table row to find p_value
    i1 = 0;
    i2 = ny-1;
    xdif1 = T2[ix][i1] - p_value;
    xdif2 = T2[ix][i2] - p_value;
    if (xdif1 * xdif2 < 0)
      // Use bisection to find the nearest cell
     {
      do
       { 
 	im = (i1 + i2) / 2;
        xdifm = T2[ix][im] - p_value;
        if (xdif1 * xdifm < 0)
          {i2 = im;}
        else
          {
		i1 = im;
          	xdif1 = xdifm;
	   }

       }while((i2-i1)!=1);
      // Interpolate in x
      fp = (p_value - T2[ix][i1]) / (T2[ix][i2] - T2[ix][i1]);
     }
    else
     {
      if (warning)
       {
        fprintf(stderr,"*** WARNING ***\n Argument to find_value_from_table_alt outside the range of the table.\n Using truncated value. No more warnings will be issued.\n");
        warning = false;
       }
      if (xdif1 >= 0)
        {fp = 0.0 ;}
      else
        {fp = 1.0 ;}
     }
    

    y_lt = (1.0  - fp) * y[ix][i1] + fp * y[ix][i2];

    ix = index_gt;
    // Scan through table row to find p_value
    i1 = 0;
    i2 = ny-1;
    xdif1 = T2[ix][i1] - p_value;
    xdif2 = T2[ix][i2] - p_value;
    if (xdif1 * xdif2 < 0) 
      // Use bisection to find the nearest cell
     {
      do
       { 
	im = (i1 + i2) / 2;
        xdifm = T2[ix][im] - p_value;
        if (xdif1 * xdifm < 0)
          {i2 = im;}
        else
          {
	   i1 = im;
           xdif1 = xdifm;
	  }
       }while((i2-i1)!=1);
      // Interpolate in x
      fp = (p_value - T2[ix][i1]) / (T2[ix][i2] - T2[ix][i1]);
     } 
    else
     {
      if (warning)
       { 
        fprintf(stderr,"*** WARNING ***\n Argument to find_value_from_table_alt outside the range of the table.\nUsing truncated value. No more warnings will be issued.\n");
        warning = false;
       }
      if (xdif1 >= 0)
        {fp = 0.0 ;}
      else
        {fp = 1.0 ;}
     }

    y_gt = (1.0  - fp) * y[ix][i1] + fp * y[ix][i2];

    // Interpolate in x

    y_interp = (1.0  - fx) * y_lt + fx * y_gt;

    value = pow(10.0,y_interp);
    return value;
}

Scalar calculate_photon_energy(Scalar eta, Scalar gamma, int n_sample_eta, int n_sample_chi, Scalar log_eta[], Scalar log_chi[][100], Scalar T2[][100])
{ 
  Scalar energy;
  Scalar rand_seed=(rand()/(double)RAND_MAX);
  Scalar chi_final;
  chi_final = find_value_from_table_alt(eta, rand_seed, n_sample_eta, n_sample_chi, log_eta, log_chi, T2);
  energy = (2.0*chi_final/eta)*gamma;
  return energy;
}

#endif

#endif
