# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:36:49 2018

@author: pia carstens
"""
# programming challenge - task 2 - combined weather and football

import numpy as np

class programming_challenge:
    result = 'unknown'
    
    def __init__(self,filename,h_target,h_val1,h_val2):
        """ filename: input file in csv format
            h_val1 and h_val2: we are looking for the difference of those two 
                columns
            h_target: header name of target value """
        self.f = open(filename)
        self.h_target = h_target
        self.h_val1 = h_val1
        self.h_val2 = h_val2
    
    def get_data(self):
        """ get header indices and extract 3 data columns """
        header = self.f.readline()
        header_fields = header.split(",")
        idx_target = header_fields.index(self.h_target)
        idx_val1 = header_fields.index(self.h_val1)
        idx_val2 = header_fields.index(self.h_val2)

        self.target_value  = []
        self.val1 = []
        self.val2 = []
        for line in self.f:
            fields =line.split(",")
            self.target_value.append(fields[idx_target])
            self.val1.append(int(fields[idx_val1]))
            self.val2.append(int(fields[idx_val2]))
    
    def get_result(self):
        """ get the target_value of the minimum difference between val1 and val2 """
        val_diff = list(abs(np.subtract(self.val1,self.val2)))
        idx_min_val_diff = val_diff.index(min(val_diff))
        
        self.result = self.target_value[idx_min_val_diff]

    
if __name__ == "__main__":
    
    # weather challenge
    weather_challenge  = programming_challenge('weather.csv','Day','MxT','MnT')
    weather_challenge.get_data()
    weather_challenge.get_result()
    print('Day of minimum temperature spread: ', weather_challenge.result)
    
    # football challenge
    football_challenge = programming_challenge('football.csv','Team','Goals','Goals Allowed')
    football_challenge.get_data()
    football_challenge.get_result()
    print('Team with smalles goal spread: ', football_challenge.result)
