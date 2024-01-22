function mydatacollection(human_index,action_index,action_num_se,loop_index,frame_num, periodicity,base_path)
dir_name = strcat(human_index,'_',action_index,'_',action_num_se(loop_index));  % Folder name, e.g. 01_01_01_15
data_path = strcat(base_path, dir_name); % Base path + Folder name 
mkdir(data_path)
frame_time = zeros(2, 6);

%% Init mmWave
data_path_lua = strcat(data_path, '\\','adc_data.bin');
RSTD_DLL_Path='~\\mmwave_studio_02_01_01_00\\mmWaveStudio\\Clients\\RtttNetClientController\\RtttNetClientAPI.dll';
mmWave_DCA1000ARM = strcat('ar1.CaptureCardConfig_StartRecord("', data_path_lua,  '", 1)');
mmWave_trigger_lua = 'ar1.StartFrame()';

ErrStatus = Init_RSTD_Connection(RSTD_DLL_Path);
if (ErrStatus ~= 30000)
    error('Error inside Init_RSTD_Connection');
end
ErrStatus =RtttNetClientAPI.RtttNetClient.SendCommand(mmWave_DCA1000ARM);
pause(2);
disp('mmWave configuring finished');

frame_time(1,:) = clock;        % Timestamps
ErrStatus =RtttNetClientAPI.RtttNetClient.SendCommand(mmWave_trigger_lua);
pause(frame_num*periodicity);
disp('Data collecting finished');

%% Record time log
t_fid = fopen(strcat(data_path, '/time_log.txt'), 'w');
for i = 1 : 1
    fprintf(t_fid, '%s\n', datestr(frame_time(i, :), 'yyyy mm dd HH MM SS fff'));
end
fclose(t_fid);
