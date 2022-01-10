#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 17:47:09 2021

@author: johannleidenfrost
"""

from scipy.stats import spearmanr
import numpy as np

data_filename = 'NoOutliersAgeVSSurvivalAllSexesAllGenes.csv'

data = np.genfromtxt(data_filename,delimiter = ',')

# removes empty spaces
x1_values = [66252, 48412, 40088, 52226, 48703, 58377, 46820, 54940, 52002, 56365, 66787, 56023, 49544, 81219, 58121, 56763, 50407, 50482, 60524, 53601, 58675, 54646, 52685, 60231, 54524, 59510, 61633, 60075, 49462, 116100, 86553, 55522, 56027, 61359, 64944, 79944, 52620, 55967, 54028, 104486, 68666, 68991, 82783, 93024, 107740, 84291, 65499, 57714, 52327, 54545, 53663, 101031, 57426, 62999, 60240, 64304, 61024, 57258, 59449, 96610, 58052, 56563]
x2_values = [2.0, 2.0, 5.0, 3.0, -1.0, 4.0, 1.0, 8.0, 7.0, 3.0, 1.0, 3.0, 5.0, 4.0, 5.0, -3.0, 3.0, 3.0, 0.0, 5.0, -4.0, 3.0, 3.0, 2.0, 1.0, 4.0, 3.0, 3.0, 10.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 3.0, 10.0, 1.0, 3.0, 0.0, 2.0, 0.0, 1.0, 1.0, 3.0, 11.0, 0.0, 5.0, 3.0, 2.0, 1.0, 3.0, -2.0, 2.0, 6.0, -3.0, 1.0, 1.0, 2.0, -3.0]

x1_values = np.array([a for a in x1_values if not np.isnan(a)])
x2_values = np.array([a for a in x2_values if not np.isnan(a)])

coef, p = spearmanr(x1_values, x2_values)
print('Spearmans correlation coefficient: %.3f' % coef)
print('P-value: %.3f' % p)
sizes = [1,2,3]
biases = [np.random.randn(y, 1) for y in sizes[1:]]
print(biases)
weights = [np.random.randn(y, x) 
                        for x, y in zip(sizes[:-1], sizes[1:])]
print(weights)