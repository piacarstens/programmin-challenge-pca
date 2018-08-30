% -----------------------------------------------------------
% Matlab skript - weather challenge - Pia Carstens, 30.8.2018
% -----------------------------------------------------------


% read weather-file
weather_data = csvread('S:\USERS\pcarstens\zeuch\weather.csv',1,0,'A2..C31');weather_data = csvread('S:\USERS\pcarstens\zeuch\weather.csv',1,0,'A2..C31');

day = weather_data(:,1);
min_T = weather_data(:,2);
max_T = weather_data(:,3);

% find smallest temperature spread
[min_dT,idx_min_dT] = min(abs(min_T-max_T));

% get day of smallest temperature spread
day_min_dT = weather_data(idx_min_dT,1);

% output day nr to command window
disp(['day of smallest temperature spread: ' num2str(day_min_dT)])
