 close all;
 clc;
 clear all;
 
for i=10000:19999
    a=num2str(i);
    num=a(2:5);
    filename1 = 'F:\Matlab SDF\Data_TNSA_2d\';
    if exist([filename1,num,'.sdf'],'file')  
    hq=GetDataSDF([filename1,num,'.sdf']);
    t=hq.time;
    m=length(hq.Grid.Grid.x);
    n=length(hq.Grid.Grid.y);
%hydrogen density
figure(1);
x1=[hq.Derived.Number_Density.hydrogen.grid.x(1:(m(1,1)-1))+hq.Derived.Number_Density.hydrogen.grid.x(2:m(1,1))]/2;
y1=[hq.Derived.Number_Density.hydrogen.grid.y(1:n(1,1)-1)+hq.Derived.Number_Density.hydrogen.grid.y(2:n(1,1))]/2;
contour(x1/1e-6,y1/1e-6,(hq.Derived.Number_Density.hydrogen.data)',10,'LineWidth',1,'Fill','on');
xlabel('x (\mum)');
ylabel('y (\mum)');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
colormap(jet);
colorbar;
ylabel(colorbar,'Density (m^{-3})');
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
set(gcf,'paperposition',[0.635,6.35,30,18]);
filename = 'F:\jpg\density';
if  exist (filename);
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','hydrogen density',num2str(1e15*t),'fs','.jpg']);
close all;
%electron density
figure(2);
x1=[hq.Derived.Number_Density.electron.grid.x(1:(m(1,1)-1))+hq.Derived.Number_Density.electron.grid.x(2:m(1,1))]/2;
y1=[hq.Derived.Number_Density.electron.grid.y(1:n(1,1)-1)+hq.Derived.Number_Density.electron.grid.y(2:n(1,1))]/2;
contour(x1/1e-6,y1/1e-6,(hq.Derived.Number_Density.electron.data)',10,'LineWidth',1,'Fill','on');
xlabel('x (\mum)');
ylabel('y (\mum)');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
colormap(jet);
colorbar;
ylabel(colorbar,'Density (m^{-3})');
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
set(gcf,'paperposition',[0.635,6.35,30,18]);
filename = 'F:\jpg\density';
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