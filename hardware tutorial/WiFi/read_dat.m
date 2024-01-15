clc;
clear;
csi_trace = read_bf_file('name.dat');
len = length(csi_trace)
ant_csi = zeros(30,len,3);
for j=1:3
  for i=1:len
    if(isempty(csi_trace{i}))
        break;
    end
    csi_entry = csi_trace{i};
    csi = get_scaled_csi(csi_entry);
    csi =csi(1,:,:);
    csi1=abs(squeeze(csi).');
    ant_csi(:,i,j)=csi1(:,j);  
  end 
  subplot(3,1,j);
  plot(ant_csi(:,:,j).');
  hold on
end
% To save the csi as a .csv file, uncomment the following two lines
% dstDir = strcat(path_to_save,'.csv')
% writematrix(ant_csi,dstDir);
size(ant_csi);
