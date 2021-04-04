# author: github.com/teo113
# desc: This script utilises the pandas module for various tasks.

import pandas as pd
import numpy as np

csv_file = r'data/list.csv'

# use pandas to read a csv file in as a data frame (df)
df = pd.read_csv(f'{csv_file}')
print(df)
# replace NaN values with empty strings
df1 = df.replace(np.nan, '', regex=True)
print(df1)
