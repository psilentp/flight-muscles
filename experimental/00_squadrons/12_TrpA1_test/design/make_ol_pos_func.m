clear all;
fs = filesep;

pathmap = containers.Map();
pathmap('win32') = 'Pcontrol_paths_win.mat' 
pathmap('win64') = 'Pcontrol_paths_win.mat'
pathmap('maci64') = 'Pcontrol_paths_mac.mat'
load(pathmap(computer('arch')));

update_freq = 60;
trial_duration = 2.0;
open_loop_duration = 0.5;
times = -1*trial_duration:1/update_freq:-0.001;
func_path = function_path;
epoch = sum(times>(-1 * open_loop_duration)) %number of samples in the epoch
null_func = double([times>(-1 * open_loop_duration)]); %mask for the movement epoch 
null_func(times>(-1 * open_loop_duration)) = 1:epoch; %linear ramp from 1 to number of samples in the epoch
null_func = [null_func,zeros(1,60)*null_func(end)]; %cat the ramp with a static pattern
func = mod(null_func,161); % 
save([ func_path fs 'position_function_starfield_2_5sec.mat'], 'func');