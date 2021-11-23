#!/usr/bin/env python3

import os
import sys
import pandas as pd

filenames = sys.argv[1:]

# Create CSV with samples for each incoming CSV
for filename in filenames:
    sample_filename = 'sampled/sample_' + filename

    if (os.path.exists(sample_filename)):
        print('Skipping %s (sample was already created)' % (filename))
        continue

    print('Reading %s' % (filename))
    # Use "latin-1" encoding to avoid decode errors
    df = pd.read_csv(filename, encoding = 'latin-1')

    print('Sampling %s' % (filename))
    df_sample = df[(df['DepDelay'] > 0.0) & (df['DepDelay'].notnull())].sample(1000, random_state=747)

    print('Sample DataFrame info:')
    print(df_sample.info())

    print('Writing intermediate CSV file %s' % (sample_filename))
    df_sample.to_csv(sample_filename, index=False)

    # Print empty line between each file
    print('')

samples_df = pd.DataFrame()
# Combine CSV with samples into final dataset
for filename in filenames:
    sample_filename = 'sampled/sample_' + filename

    print('Reading %s' % (sample_filename))
    # Use "latin-1" encoding to avoid decode errors
    df = pd.read_csv(sample_filename, encoding = 'latin-1')

    print('Sample DataFrame info:')
    print(df.info())

    print('Appending rows')
    samples_df = samples_df.append(df, ignore_index=True)
    
print('Writing combined CSV')
samples_df.to_csv('sampled/combined.csv') 

print('Combined CSV info:')
print(samples_df.info())
