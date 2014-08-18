clear all
flynum = 169;
datestr = '20140605';
rootdir = strcat('G:\FlyDB','\Fly',num2str(flynum,'%04d'));
exp_label = 'rotating_starfield_imaging_T2_trial_2';
datafilename = strcat(rootdir,'\fly',num2str(flynum,'%04d'),'_', exp_label);
one_volt = (32766-200)/10;

starfield_names = {'static_test_90.mat'
                   'static_test_270.mat'
                   'stripe_test_90.mat'
                   'stripe_test_270.mat'
                   'opti_test_90.mat'
                   'opti_test_270.mat'
};

fixation_pattern = 1;
[num_starfield_patterns,n] = size(starfield_names)
starfield_pattern = 2;
volts_per_pat = 10/num_starfield_patterns;

open_loop_update_freq = 60;

%% pattern params needed to set the laser trigger
%pixels in actual pattern
azmuth_pix = 8*12;
gs_val = 3;
x_num = azmuth_pix*(2^gs_val);%same as image Azm
DegPerXstp = 360/x_num;
ThreshAngle = 40;
threshX = floor(DegPerXstp*ThreshAngle);

%% Closed loop
Panel_com('stop');pause(0.005);
Panel_com('set_AO',[3 int16(one_volt*-1)])
Panel_com('laser_off');
Panel_com('set_pattern_id',fixation_pattern);pause(0.005); %stripe fixation pattern
Panel_com('set_mode',[1 1]);pause(0.05); %set closed loop X closed loop Y
Panel_com('set_velfunc_id',[0 0]);pause(0.01); %use default function on x and y channel (is this nessessary?)
Panel_com('send_gain_bias',[-100.0,0,0,0]);pause(0.005);%
Panel_com('set_position',[48 1]);pause(0.005); % start at close to fixation
Panel_com('set_AO',[3 int16(one_volt*-1)])
Panel_com('start');
pause(20);

record_index = 1;
Panel_com('send_laser_pattern' ,[ones(1,96)]');
Panel_com('set_funcx_freq', open_loop_update_freq)
for rep = 1:12
    for i = datasample([1:num_starfield_patterns,;ones(1,num_starfield_patterns)],num_starfield_patterns,2,'replace',false)
        starfield_pattern = i(1)+1;
        open_loop_function = i(2);
        datarecord(record_index).open_loop_function = open_loop_function;
        datarecord(record_index).starfield_name = starfield_names{i(1)};
        datarecord(record_index).start_time = now;
        disp(datarecord(record_index).starfield_name);
        
        %% Closed loop
        Panel_com('stop');pause(0.001);
        Panel_com('laser_off');
        Panel_com('set_pattern_id',fixation_pattern);pause(0.001); %stripe fixation pattern
        Panel_com('set_mode',[1 0]);pause(0.001); %set closed loop X open loop Y
        Panel_com('set_velfunc_id',[0 0]);pause(0.001); %use default function on x and y channel (is this nessessary?)
        Panel_com('send_gain_bias',[-100.0,0,0,0]);pause(0.001);%
        Panel_com('set_position',[48 1]);pause(0.001); % start at close to fixation
        Panel_com('set_AO',[3 int16(one_volt*-1)])
        Panel_com('start');
        pause(5);
        
        %disp('here')
        %% Start starfield
        Panel_com('stop');pause(0.001)
        Panel_com('set_AO',[3 int16(one_volt*volts_per_pat*i(1))]);pause(0.001)
        Panel_com('set_pattern_id',starfield_pattern);pause(0.001); %set to expansion pattern 
        Panel_com('set_position',[1 1]);pause(0.001); %set the x position at begining y posistion is an exp parameter
        Panel_com('set_mode',[1 4]);pause(0.001); %set the x mode to function based position control mode
        Panel_com('send_gain_bias',[-50.0,0,0,0]);pause(0.001); %set the gain and bias to zero for both X and Y
        Panel_com('set_posfunc_id',[2 open_loop_function])%pause(0.001); %position function to run on channel 2 (y)
        Panel_com('set_funcx_freq', 60);pause(0.001);
        Panel_com('start');
        pause(3.1);

        record_index = record_index+1;
    end
end

%% Put the fly back into closed loop.
Panel_com('stop');pause(0.005);
Panel_com('set_AO',[3 int16(one_volt*-1)])
Panel_com('laser_off');
Panel_com('set_pattern_id',fixation_pattern);pause(0.005); %stripe fixation pattern
Panel_com('set_mode',[1 1]);pause(0.05); %set closed loop X closed loop Y
Panel_com('set_velfunc_id',[0 0]);pause(0.01); %use default function on x and y channel (is this nessessary?)
Panel_com('send_gain_bias',[-50.0,0,0,0]);pause(0.005);%
Panel_com('set_position',[48 1]);pause(0.005); % start at close to fixation
Panel_com('start');
pause(10);

%save(datafilename,'exp_label', 'datarecord');