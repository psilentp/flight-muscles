clear all

pattern_names = {'static_test_roll_90.mat'
                 'static_test_roll_270.mat'
                 'static_test_yaw_90.mat'
                 'static_test_yaw_270.mat'};

for pnum = 1:6;
    pname = char(pattern_names(pnum))
    load(pname);
    psize = size(imgs)
    % make_6_wide_med_cont_pattern_48.m
    pattern.x_num = psize(3);% There are 96 pixel around the display (12x8)
    pattern.y_num = psize(4) %first y is the cl yaw, the rest are the rotation patterns
    pattern.num_panels = 48; 	% This is the number of unique Panel IDs required.
    pattern.gs_val = 3; 	% This pattern will use 8 intensity levels
    pattern.row_compression = 0;

    Pats = zeros(psize(1), psize(2), pattern.x_num, pattern.y_num);
    Pats(:,:,:,:) = imgs;
    pattern.Pats = Pats;

    pattern.Panel_map = [12 8 4 11 7 3 10 6 2  9 5 1; 24 20 16 23 19 15 22 18 14 21 17 13; 36 32 28 35 31 27 34 30 26 33 29 25; 48 44 40 47 43 39 46 42 38 45 41 37];
    pattern.BitMapIndex = process_panel_map(pattern);
    disp('making pattern vector')
    pattern.data = Make_pattern_vector(pattern);
    directory_name = 'C:\Users\flyranch\panels\Matlab Codes\Patterns';
    str = [directory_name '\Pattern_scld_' pname(1:end-4)]
    save(str, 'pattern');
    clear Pats
    clear pattern
    clear imgs
end