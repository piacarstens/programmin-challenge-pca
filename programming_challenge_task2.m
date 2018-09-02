
% -----------------------------------------------------------
% Matlab skript - programming challenge - Task 2
% Pia Carstens, 30.8.2018
%
% additionally to task 1 (weather challenge) this programm
% solves the task for both the weather and the football challenge
%
% what it does: - read input file (csv format)
%               - calculate the difference between two specified
%                 values listed in the header
%               - output value associated with minimum difference
%                 as specified by another header value
% -----------------------------------------------------------

%% --- initialise ---------------------
% input files
weather.file = 'S:\USERS\pcarstens\zeuch\weather.csv';
football.file = 'S:\USERS\pcarstens\zeuch\football.csv';

% assign val1 and val2 which are the header values we are interested in
football.val1 = 'Goals';            
football.val2 = 'Goals Allowed';
weather.val1 = 'MxT';
weather.val2 = 'MnT';

% assign target_value which is the output value we are looking for
football.target_value = 'Team';
weather.target_value = 'Day';

%% --- get result and display -----------
% call function get_result
football.result = get_result(football);
weather.result  = get_result(weather);

% display result
disp(['Name of Team: ' char(football.result)])
disp(['Day: ', num2str(weather.result)])
 
%% --------------------------------------
% this function returns the target_value that is associated with the
% minimum difference between val1 and val2

function [result] = get_result(indata)

% read file
T = readtable(indata.file,'Delimiter',',');

% find smallest difference between val1 and val2
[~,idx_min_diff] = eval(['min(abs(T.' indata.val1 '-T.' regexprep(indata.val2,' ','') '))']);

% get target value of smallest difference
result =  eval(['T.' indata.target_value '(' num2str(idx_min_diff) ')']);

end
