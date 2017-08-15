 close all;
 clc;
 clear all;
 
for i=10000:19999
    a=num2str(i);
    num=a(2:5);
    filename1 = 'F:\Matlab SDF\Data_TNSA\';
    if exist([filename1,num,'.sdf'],'file')  
    hq=GetDataSDF([filename1,num,'.sdf']);
    t=hq.time;
    m=length(hq.Grid.Grid.x);
%hydrogen density
figure(1);
x1=[hq.Derived.Number_Density.proton.grid.x(1:(m(1,1)-1))+hq.Derived.Number_Density.proton.grid.x(2:m(1,1))]/2;
plot(x1/1e-6,(hq.Derived.Number_Density.proton.data)','-r','LineWidth',2);
xlabel('x (\mum)');
ylabel('Density (m^{-3})');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
set(gcf,'paperposition',[0.635,6.35,30,18]);
filename = 'F:\TNSA\density';
if  exist (filename);
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','hydrogen density',num2str(1e15*t),'fs','.jpg']);
close all;
%electron density
figure(2);
x1=[hq.Derived.Number_Density.electron.grid.x(1:(m(1,1)-1))+hq.Derived.Number_Density.electron.grid.x(2:m(1,1))]/2;
plot(x1/1e-6,(hq.Derived.Number_Density.electron.data)','-r','LineWidth',2);
xlabel('x (\mum)');
ylabel('Density (m^{-3})');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
set(gcf,'paperposition',[0.635,6.35,30,18]);
filename = 'F:\TNSA\density';
if  exist (filename)
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','electron density',num2str(1e15*t),'fs','.jpg']);
close all;
clear all;
    else
        continue
    end
end