clc;clear;close all;
%% Parameters
base_path = '';
params = readcell("params.txt");
human_index = num2str(params{1,1},'%02d');
action_index = num2str(params{2,1},'%02d');
is_five = params{3,1};
if is_five == 1
    action_num_se = ["01_10","11_20"];  
else
    action_num_se = ["01_05","06_10","11_15","16_20"];   
end
time_label = datenum(params{4,1}+params{4,2});    % Start Time which is same as PC1
time_label = time_label - datenum(seconds(2));    % Start two seconds early for configuration.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
periodicity = 50*0.001;                        
start_collect = false;
loop_num = length(action_num_se);              

% Remember to change frame_num setting in mmWave studio
if(loop_num == 2)                              % 5s, frame_num=1180
    frame_num = 59/periodicity;         
elseif(loop_num == 4)                          % 10s,frame_num=1080
    frame_num = 54/periodicity;
end

%% Loop
curr_loop_num = 0;
while(true)
    if(time_label < datenum(datestr(now, 'yyyy-mm-dd HH:MM:SS.fff'))) % Start Collecting
        if(curr_loop_num >= loop_num)
            break;
        else
            curr_loop_num = curr_loop_num + 1;
        end
        mydatacollection(human_index,action_index,action_num_se,curr_loop_num,frame_num,periodicity,base_path);
        a = datevec(time_label) + [0 0 0 0 0 frame_num*periodicity+10]; % Wait 10 seconds for restarting
        time_label = datenum(a);
    end
end
sprintf("Collection End");