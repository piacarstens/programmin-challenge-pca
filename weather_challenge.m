% -----------------------------------------------------------
% Matlab skript - weather challenge - Pia Carstens, 30.8.2018
% -----------------------------------------------------------


% read weather-file
weather_data = csvread('S:\USERS\pcarstens\zeuch\weather.csv',1,0);

% find smallest temperature spread
[min_dT,idx_min_dT] = min(abs(weather_data(:,2)-weather_data(:,3)));

% output day of smallest temperature spread to command window
disp(['day of smallest temperature spread: ' num2str(weather_data(idx_min_dT,1))])
