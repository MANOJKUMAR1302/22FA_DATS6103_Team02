#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %% 
# Check dataset
df = pd.read_csv("salary_data")
df.info()
df.isnull().sum()
df.head()


list(set(list(df['title'])))
# ['Management Consultant', 'Marketing', 'Product Designer', 'Human Resources', 'Product Manager', 'Software Engineering Manager', 'Solution Architect', 'Business Analyst', 'Sales', 'Hardware Engineer', 'Mechanical Engineer', 'Recruiter', 'Data Scientist' 'Technical Program Manager', 'Software Engineer']
len(list(set(list(df['title'])))) # 15

list(set(list(df['location']))) 
len(list(set(list(df['location'])))) # 1050
list(df['location'])[0].split(', ')[1]

# Preprocessing data


# %%
# Is salary affected by the role offered? 

avgbytitle = df.groupby('title').mean()
print (avgbytitle)

avgsalary = avgsalary = df.groupby('title').mean()['yearlysalary'].reset_index()
print (avgsalary)

avgsalary.plot(kind = 'bar', x = 'title', y = 'yearlysalary', title = 'Average Salary per Job Title', figsize=(15,8))
plt.show()

# check correlation between yearofexperience and title 


#%% 
# Does location impact the salaries of the employees? 

# States in US
# Comparing between US states

# Countries
# Comparing between coountires (US, Europe, India, etc..)