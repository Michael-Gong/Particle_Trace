 close all;
 clc;
 clear all;
 filename1 = 'F:\Matlab SDF\Data_TNSA_2d\';
for i=10000:19999
    a=num2str(i);
    num=a(2:5);
    if exist([filename1,num,'.sdf'],'file')  
    hq=GetDataSDF([filename1,num,'.sdf']);
    t=hq.time;
%hydrogen theta_energy
figure(1)
image(hq.dist_fn.theta_en.hydrogen.grid.x/pi,hq.dist_fn.theta_en.hydrogen.grid.y/1.6e-13,(hq.dist_fn.theta_en.hydrogen.data)');
xlabel('Theta (rad)');
ylabel('Energy (MeV)');
set(gca,'ydir','normal');
colormap(jet);
colorbar;
ylabel(colorbar,'Number (a.u.)');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
set(gcf,'paperposition',[0.635,6.35,30,18]);
filename = 'F:\jpg\theta_energy';
if  exist (filename)
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','hydrogen theta_energy',num2str(1e15*t),'fs','.jpg']);
close all;
%electron theta_energy
figure(2)
image(hq.dist_fn.theta_en.electron.grid.x/pi,hq.dist_fn.theta_en.electron.grid.y/1.6e-13,(hq.dist_fn.theta_en.electron.data)');
xlabel('Theta (rad)');
ylabel('Energy (MeV)');
set(gca,'ydir','normal');
colormap(jet);
colorbar;
ylabel(colorbar,'Number (a.u.)');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
set(gcf,'paperposition',[0.635,6.35,30,18]);
filename = 'F:\jpg\theta_energy';
if  exist (filename)
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','electron theta_energy',num2str(1e15*t),'fs','.jpg']);
close all;
    else
        continue
    end
end