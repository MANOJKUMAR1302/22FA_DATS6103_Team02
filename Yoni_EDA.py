#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %% 
# Check dataset
df = pd.read_csv("salary_data.csv")
df.info()
df.isnull().sum()
df.head()


list(set(list(df['title'])))
len(list(set(list(df['title'])))
)
list(set(list(df['location'])))
len(list(set(list(df['location']))))


# Preprocessing data
# %%
# Is salary affected by the role offered? 

avgbytitle = df.groupby('title').mean()
avgbytitle

avgsalary = avgsalary = df.groupby('title').mean()['yearlysalary'].reset_index()





#%% 
# Does location impact the salaries of the employees? 

# States in US
# Comparing between US states

# Countries
# Comparing between coountires (US, Europe, India, etc..)