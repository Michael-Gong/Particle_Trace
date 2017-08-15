 close all;
 clc;
 clear all;
filename1 = 'F:\Matlab SDF\Data_TNSA\';
for i=10000:19999
    a=num2str(i);
    num=a(2:5);
    if exist([filename1,num,'.sdf'],'file')  
    hq=GetDataSDF([filename1,num,'.sdf']);
    t=hq.time;
%hydrogen energy
figure(1)
semilogy(hq.dist_fn.en.proton.grid.x/1.6e-13,hq.dist_fn.en.proton.data,'-r','LineWidth',2);
xlabel('Energy (MeV)');
ylabel('Number (a.u.)');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
set(gcf,'paperposition',[0.635,6.35,30,18]);
filename = 'F:\TNSA\energy';
if  exist (filename)
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','hydrogen energy',num2str(1e15*t),'fs','.jpg']);
close all;
%electron energy
figure(2)
semilogy(hq.dist_fn.en.electron.grid.x/1.6e-13,hq.dist_fn.en.electron.data,'-r','LineWidth',2);
xlabel('Energy (MeV)');
ylabel('Number (a.u.)');
box(gca,'on');
set(gca,'LineWidth',2);
set(gca,'Fontsize',24,'FontWeight','bold','XColor',[0 0 0],'YColor',[0 0 0],'ZColor',[0 0 0]);
title(['t = ',num2str(1e15*t),' fs'],'FontWeight','bold');
set(gcf,'paperposition',[0.635,6.35,30,18]);
filename = 'F:\TNSA\energy';
if  exist (filename)
else
    mkdir (filename);
end
saveas(gcf,[filename,'\','electron energy',num2str(1e15*t),'fs','.jpg']);
close all;
    else
        continue
    end
end