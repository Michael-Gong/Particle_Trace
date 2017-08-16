pro michael
x=fltarr(10002,2500)
y=fltarr(10002,2500)
t1=read_ascii('./x.txt')
t2=read_ascii('./y.txt')
x=reform(t1.field1,[10002,2500])
y=reform(t2.field1,[10002,2500])
save,x,y,filename='./x_y.sav'
end
