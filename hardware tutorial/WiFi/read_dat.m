r_path = 'D:\pythonProject1';
data_path = strcat(r_path,'\sample_data\','07_01_12','.dat');
csi_trace = read_bf_file(data_path);
len = length(csi_trace)
% length = len / 10000;
ant_csi = zeros(30,len,3);
% figure(1);
for j=1:3
  for i=1:len
    if(isempty(csi_trace{i}))
        break;
    end
    csi_entry = csi_trace{i};
    csi = get_scaled_csi(csi_entry); % [1,3,30]    
    csi =csi(1,:,:); %csi_shape=[3,30]
    csi1=abs(squeeze(csi).'); % csi1_shape=[30,3]

    ant_csi(:,i,j)=csi1(:,j);%ant_csi=[30,990]     
  end 
  subplot(3,1,j);
  plot(ant_csi(:,:,j).');
  hold on
end
% To save the csi as a .csv file, uncomment the following two lines
% dstDir = strcat(path_to_save,'.csv')
% writematrix(ant_csi,dstDir);
size(ant_csi);