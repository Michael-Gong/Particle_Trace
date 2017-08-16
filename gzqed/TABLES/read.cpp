#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>

using namespace std;
int main()
{
	ifstream ifile("./hsokolov.table");
	if(! ifile)
	{  cerr<<"error."<<endl;
	   return -1;
	}

	int h_sample;
	double min,max;
        ifile>>h_sample;
	double hsokolov[h_sample][2];
	ifile>>min; ifile>>max;
	for(int i=0;i<=h_sample-1;i++)
	  { 
	    ifile>>hsokolov[i][0];
	    ifile>>hsokolov[i][1];
	  }	

        ifile.close();
	ifile.clear();

	cout<<"h_sample is "<<h_sample<<endl;
	cout<<"min and max are "<<min<<"and"<<max<<endl;
	for(int i=0;i<=h_sample-1;i++)
	  { 
	    cout<<hsokolov[i][0]<<" ; "<<hsokolov[i][1]<<endl;
	  }	

//##########################################################

	ifile.open("./ksi_sokolov.table");
	if(! ifile)
	{  cerr<<"error."<<endl;
	   return -1;
	}

	int n_sample_eta, n_sample_chi;;
	double etalog_min,etalog_max;
        ifile>>n_sample_eta; ifile>>n_sample_chi; 
	double p_photon_energy[n_sample_eta][n_sample_chi];
	ifile>>etalog_min; ifile>>etalog_max;
	for(int i=0;i<=n_sample_eta-1;i++)
	  { 
	    for(int j=0;j<=n_sample_chi-1;j++)
	      {
	  	ifile>>p_photon_energy[i][j];
	      }
	  }	
        ifile.close();
        
	cout<<"n_sample_eta and n_sample_chi are "<<n_sample_eta<<" and "<<n_sample_chi<<endl;
	cout<<"etalog_min and etalog_max are "<<etalog_min<<" and "<<etalog_max<<endl;
	for(int i=0;i<=1;i++)
	  { 
	    for(int j=0;j<=n_sample_chi-1;j++)
	      {
	        cout<<setprecision(10)<<p_photon_energy[i][j]<<" ; ";
	      }
	    cout<<"*****"<<endl;
	  }
	
//###########################################################

	ifile.open("./chimin.table");
	if(! ifile)
	{  cerr<<"error."<<endl;
	   return -1;
	}
        double chimin_table[n_sample_eta];
	for(int i=0;i<=n_sample_eta-1;i++)
	  { 
	    ifile>>chimin_table[i];
	  }	
	ifile.close();

	cout<<"chimin.table!"<<endl;
	    for(int j=0;j<=n_sample_eta-1;j++)
	      {
	        cout<<setprecision(10)<<chimin_table[j]<<" ; ";
	      }

	
return 0;
}

