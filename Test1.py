# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 21:32:32 2018

@author: Nimme
"""
#Reading data
import os
os.chdir('C:\\Users\\Nimme\\Documents\\Python')

import pandas
nm = pandas.read_csv('TestData.csv')
print(nm)
nm.head()

#Renaming columns
nm.rename({'mpg':'milepergallon', 'cyl':'cylinder', 'disp':'dispensation'}, axis='coloumns')
nm = nm.rename(columns={'mpg': 'milepergallon', 'cyl': 'cylinder'})
print(nm)

#subsetting
n1 = nm.query('milepergallon > 20')
print(n1)

#using or statement
n2 = nm[(nm.cylinder == 4) | (nm.cylinder == 6)]

#Removing column
n3 = nm.drop('hp', 1)
print(n3)

n4 = nm.drop('cylinder', 1)
print(n4)

#promting for input    
n2 = int(input('Insert number of cylinder'))
if n2==4:
    n3=nm.query('cylinder == 4')
elif n2==6:
    n3=nm.query('cylinder == 6')   







