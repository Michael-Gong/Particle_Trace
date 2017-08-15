 close all;
 clc;
 clear all;
 filename1 = 'F:\Matlab SDF\Data_RPA\';
for i=10000:19999
    a=num2str(i);
    num=a(2:5);
    if exist([filename1,num,'.sdf'],'file')  
    hq=GetDataSDF([filename1,num,'.sdf']);
    t=hq.time;
%hydrogen x_px
m0=9.10938291e-31;
c=2.99792458e8;
figure(1)
contour(hq.dist_fn.x_px.proton.grid.x/1e-6,hq.dist_fn.x_px.proton.grid.y/(m0*c),(hq.dist_fn.x_px.proton.data)',10,'LineWidth',1,'Fill','on');
xlabel('x (\mum)');
ylabel('p_x (m_ec)');
set(gca,'ydir','normal');
colormap(jet);
colorbar;
ylabel(colorbar,'Number');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
filename = 'F:\RPA\phase';
if  exist (filename)
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','hydrogen x_px',num2str(1e15*t),'fs','.jpg']);
close all;
%electron x_px
m0=9.10938291e-31;
c=2.99792458e8;
figure(2)
contour(hq.dist_fn.x_px.electron.grid.x/1e-6,hq.dist_fn.x_px.electron.grid.y/(m0*c),(hq.dist_fn.x_px.electron.data)',10,'LineWidth',1,'Fill','on');
xlabel('x (\mum)');
ylabel('p_x (m_ec)');
set(gca,'ydir','normal');
colormap(jet);
colorbar;
ylabel(colorbar,'Number');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
filename = 'F:\RPA\phase';
if  exist (filename)
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','electron x_px',num2str(1e15*t),'fs','.jpg']);
close all;
    else
        continue
    end
end