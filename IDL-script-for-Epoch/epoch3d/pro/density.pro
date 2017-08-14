pro density
restore,'./sav/parameter.sav'
print,'Start reading density distribution'
b=dblarr(nx,ny,(endtime-starttime)/interval+1,nspecie)
for n=0,nspecie-1 do begin
for i=0,(endtime-starttime)/interval do begin
  f='number_density_'+sname[n]
  extra=create_struct(f,1)
  a=getdata(i*interval+starttime,_extra=extra)
  a=a.(4)
  b[*,*,i,n]=a[*,*,nz/2]
  print,'finished',n*100/nspecie+(i*interval+interval)*100/((endtime-starttime+interval)*nspecie),'%'
endfor
endfor
save,b,filename='./sav/density.sav'
print,'Reading density OK !'
end
