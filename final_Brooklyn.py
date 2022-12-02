#%%

### Data Cleaning

import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
pd.set_option('display.colheader_justify', 'center')
pd.set_option('display.precision', 3)

#%%
old_df=pd.read_csv('Levels_Fyi_Salary_Data.csv',encoding='latin1')

old_df.info()
old_df.head()

#%%
df = old_df[['company','title','location','yearsofexperience','yearsatcompany']].copy()

df['yearlysalary'] = old_df['totalyearlycompensation'] + old_df['basesalary']
# %%
df.to_csv('salary_data', index=False)


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import rfit
import sklearn
from sklearn.datasets import load_boston 


rfit.dfchk(df)

#%%

# 1. Will the salary be affected by different employers?


# List all the companys in this dataframe
# print(f"the unique values:\n{pd.unique(df.company)}")



### Removing the Outliers of yearlysalary
df1 = df.copy()
print ("Shape Of The Before Ouliers: ",df.shape)
n=1.5
IQR_1 = np.percentile(df1['yearlysalary'],75) - np.percentile(df1['yearlysalary'],25)
#outlier = Q3 + n*IQR 
df1=df1[df1['yearlysalary'] < np.percentile(df1['yearlysalary'],75)+n*IQR_1]
#outlier = Q1 - n*IQR 
df1=df1[df1['yearlysalary'] > np.percentile(df1['yearlysalary'],25)-n*IQR_1]
print ("Shape Of The After Ouliers: ",df1.shape)


# Removing the Outliers of yearsatcompany
df2 = df1.copy()
print ("Shape Of The Before Ouliers: ",df.shape)
n=1.5
IQR_2 = np.percentile(df2['yearsatcompany'],75) - np.percentile(df2['yearsatcompany'],25)
#outlier = Q3 + n*IQR 
df2=df2[df2['yearsatcompany'] < np.percentile(df2['yearsatcompany'],75)+n*IQR_2]
#outlier = Q1 - n*IQR 
df2=df2[df2['yearsatcompany'] > np.percentile(df2['yearsatcompany'],25)-n*IQR_2]
print ("Shape Of The After Ouliers: ",df2.shape)





# Boxplot
sns.boxplot(df['yearlysalary']).set_title('Before removing outliers')


sns.boxplot(df2['yearlysalary']).set_title('After removing outliers')



# Independent-Sample T Test (2 groups)

# Top 10 companies in the United States (https://fortune.com/fortune500/)

# H0: The means for the two populations are equal.
# H1: The means for the two populations are not equal.

import researchpy as rp
import scipy.stats as stats

top10 = df2[df2.company.isin(["Apple","apple","APPLE","Walmart Labs","Walmart","walmart","Amazon","amazon","AMAZON","CVS health","cvs health","CVS Health","UnitedHealth Group","ExxonMobil"
"McKesson"])]
rfit.dfchk(top10)

not10 = df2[~df2.company.isin(["Apple","apple","APPLE","Walmart Labs","Walmart","walmart","Amazon","amazon","AMAZON","CVS health","cvs health","CVS Health","UnitedHealth Group","ExxonMobil"
"McKesson"])]
rfit.dfchk(not10)

summary, results = rp.ttest(group1= top10['yearlysalary'], group1_name= "top10",
                            group2= not10['yearlysalary'], group2_name= "not10")

print(summary)
print(results)

# The average yearlysalary for top 10 company, M= 10345.0 , was statistically signigicantly higher than those not-top-10 companies.
# M= 320757.462; t= 23.245, p < 0.05

#%%

# 5. Is working for more years in the same company affect the salary?


# Boxplot
sns.boxplot(df['yearsatcompany']).set_title('Before removing outliers')


sns.boxplot(df2['yearsatcompany']).set_title('After removing outliers')


### Scatterplot & Linear Regression Fit Line

# Before Removing Outliers
sns.regplot(x=df["yearsatcompany"], y=df["yearlysalary"], line_kws={"color":"r","alpha":0.7,"lw":2}).set_title('Before removing outliers')
plt.show()


# After Removing Outliers
sns.regplot(x=df2["yearsatcompany"], y=df2["yearlysalary"], line_kws={"color":"r","alpha":0.7,"lw":2}).set_title('After removing outliers')
plt.show()




# calculate the Pearson's correlation between two variables
from scipy.stats import pearsonr
corr, _ = pearsonr(df2['yearsatcompany'], df2['yearlysalary'])
print('Pearsons correlation: %.3f' % corr)

# Correlation matrix
corr_matrix = df2.corr()
print(corr_matrix)

#%%

