#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:48:54 2023

@author: girubuntu
"""


import pandas as pd

# Read in the .tsv file
df = pd.read_csv('players.csv')

# display the names of the columns


columns = ['ls', 'st', 'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam', 'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm', 'rm', 'lwb', 'ldm', 'cdm',
           'rdm', 'rwb', 'lb', 'lcb', 'cb', 'rcb', 'rb']

df_columns = df.columns
print(len(df_columns))
""" for column in columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')


# Save the updated DataFrame to a new .tsv file
df.to_csv('players_bis.csv', sep='\t', index=False)
 """
