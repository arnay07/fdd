#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:48:54 2023

@author: girubuntu
"""


import pandas as pd

# Read in the .tsv file
df = pd.read_csv('CIS_CIP_bdpm.tsv', sep='\t', encoding='iso-8859-1')

# Convert the 'date' column to datetime format
df['cip5'] = pd.to_datetime(df['cip5'], format='%d-%m-%Y')

# Save the updated DataFrame to a new .tsv file
df.to_csv('CIS_CIP_bdpm_new.tsv', sep='\t', index=False)


