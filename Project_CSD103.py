#!/usr/bin/env python
# coding: utf-8

# 
# ![maths ph.png](data:image/png;base64,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)     
# 
# 
# 
# 
# 
# CSD103 Project
# 
# Team--The Trio Techs     
# 
# Bindu (12206722)
# 
# Sahana (12207127)
# 
# Monika (12223509)
# 

# In[2]:


import numpy as sns
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# In[3]:


data=pd.read_csv('hotel_bookings.csv')
data.head()


# In[4]:


data.info()


# In[5]:


data.shape


# In[6]:


data.describe()


# In[7]:


data.dtypes


# In[8]:


(data.isna().sum()*100/data.shape[0]).round(2)


# In[9]:


data[~data['agent'].notnull()]


# In[10]:


data.loc[~data['agent'].notnull(),'agent']='Anonymous'


# In[11]:


data.loc[~data['country'].notnull(),'country']='Anonymous_country'


# In[12]:


data.loc[~data['company'].notnull(),'company']='Anonymous_company'


# In[13]:


data.isna().sum()


# In[14]:


data['total_of_special_requests'].fillna(data['total_of_special_requests'].mean(),inplace=True)


# In[15]:


data.isna().sum()


# In[16]:


data[data.duplicated()]


# In[17]:


data[data['hotel'].duplicated()].shape


# In[18]:


data.nunique()


# In[19]:


numerical_variables=data.select_dtypes(['int','float'])
numerical_variables.head()


# In[20]:


catagorial_variables=data.select_dtypes('object')
catagorial_variables.head()


# In[21]:


sns.pairplot(data)


# In[58]:


sns.heatmap(numerical_variables.corr(),annot=True,fmt='.1f')
plt.title('Correlation Heatmap')
plt.show()


# In[23]:


plt.figure(figsize=(5,4))
sns.countplot(data=data,x='market_segment',width=.5)
plt.xticks(rotation=45)
plt.show()


# In[24]:


ngroup_data=data['market_segment'].value_counts().reset_index()
ngroup_data.rename(columns={'index':'market_segment','market_segment':'count'},inplace=True)


# In[25]:


ngroup_data


# In[26]:


sns.barplot(data=ngroup_data,x='market_segment',y='count',hue='market_segment')
plt.show()


# In[40]:


plt.figure(figsize=(5,3))
sns.barplot(data=data,x='distribution_channel',y='stays_in_week_nights',width=.5)
plt.title('Distribution_Channel vs Stays_in_week_nights')
plt.show()


# In[133]:


plt.figure(figsize=(5,3))
sns.lineplot(data=data,x='arrival_date_year',y='customer_type',hue='deposit_type')
plt.xticks(rotation=45)
plt.title('Customer_Type by arrival_date_year')
plt.legend(loc='upper left', prop={'size':8})
plt.show()


# In[29]:


plt.figure(figsize=(5,3))
sns.barplot(data=data,y='lead_time',x='market_segment',hue='reservation_status',dodge=False,errcolor='k',capsize=.1,errwidth=2,)
plt.xticks(rotation=45)
plt.show()


# In[125]:


#scatter plot
plt.scatter(data['arrival_date_day_of_month'], data['lead_time'])
plt.xlabel('Arrival Date Day of Month')
plt.ylabel('Lead Time')
plt.title('Scatter Plot: Arrival Date Day of Month vs Lead Time')
plt.show()


# In[126]:


# Create a histogram of 'lead_time'
plt.figure(figsize=(5,3))
plt.hist(data['lead_time'], bins=30, color='blue', edgecolor='black')
plt.title('Lead Time Distribution')
plt.xlabel('Lead Time (days)')
plt.ylabel('Frequency')
plt.show()


# In[132]:


plt.figure(figsize=(7, 5))
plt.scatter(data['adr'], data['lead_time'], alpha=0.5)
plt.xlabel('adr')
plt.ylabel('lead_time')
plt.title('adr vs lead_time')
plt.show()


# In[85]:


adr_mode = data['adr'].mode().iloc[0]

print(f"The mode of adr is: {adr_mode:.2f}")


# In[78]:


adr_mean=data['adr'].mean()
print(f"The mean adr is: {adr_mean:.2f}")


# In[79]:


adr_median=data['adr'].median()
print(f"The median adr is: {adr_median:.2f}")


# In[87]:


adr_variance=data['adr'].var()
print(f"The variance of adr is: {adr_variance:.2f}")


# In[88]:


adr_std=data['adr'].std()
print(f"The Standard variance of adr is: {adr_std:.2f}")


# In[84]:


adr_skewness = data['adr'].skew()

print(f"The skewness of adr is: {adr_skewness:.2f}")


# In[90]:


adr_kurtosis = data['adr'].kurt()

print(f"The kurtosis of adr is: {adr_kurtosis:.2f}")


# In[91]:


adr_quartiles = data['adr'].quantile([0.25, 0.5, 0.75])
adr_iqr = adr_quartiles[0.75] - adr_quartiles[0.25]

print(f"Q1 (25th percentile): {adr_quartiles[0.25]:.2f}")
print(f"Q2 (50th percentile, median): {adr_quartiles[0.5]:.2f}")
print(f"Q3 (75th percentile): {adr_quartiles[0.75]:.2f}")
print(f"IQR (Interquartile Range): {adr_iqr:.2f}")


# In[93]:


adr = data['adr']

mean = adr.mean()
median = adr.median()
mode = adr.mode()[0]

range_val = adr.max() - adr.min()
variance = adr.var()
std_dev = adr.std()
q1 = adr.quantile(0.25)
q3 = adr.quantile(0.75)
iqr = q3 - q1

skewness = adr.skew()
kurtosis = adr.kurtosis()

print(f"Measures of Central Tendency:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}\n")

print(f"Measures of Variability:")
print(f"Range: {range_val}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
print(f"IQR: {iqr}\n")

print(f"Shape of the Distribution:")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")


# In[94]:


df = data['lead_time']

mean = df.mean()
median = df.median()
mode = df.mode()[0]

range_val = df.max() - df.min()
variance = df.var()
std_dev = df.std()
q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3 - q1

skewness = df.skew()
kurtosis = df.kurtosis()

print(f"Measures of Central Tendency:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}\n")

print(f"Measures of Variability:")
print(f"Range: {range_val}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
print(f"IQR: {iqr}\n")

print(f"Shape of the Distribution:")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")


# In[36]:


data['cumulative_arrival_date_week_number']=data['arrival_date_week_number'].cumsum()


# In[37]:


data['cumulative_arrival_date_week_number']=data['arrival_date_week_number'].cummax()
data['cumulative_arrival_date_week_number']=data['arrival_date_week_number'].cummin()


# In[38]:


data[['customer_type','arrival_date_week_number','cumulative_arrival_date_week_number','cumulative_arrival_date_week_number','cumulative_arrival_date_week_number']]


# In[66]:


categorical_columns = ['hotel', 'arrival_date_month', 'customer_type']
for column in categorical_columns:
    print(data[column].value_counts())


# In[95]:


numerical_data = data[['adr', 'lead_time'] ]
statistics = numerical_data.describe()
range_values = numerical_data.max() - numerical_data.min()
variance = numerical_data.var()
standard_deviation = numerical_data.std()
skewness = numerical_data.skew()
kurtosis = numerical_data.kurtosis()

statistics['Range'] = range_values
statistics['Variance'] = variance
statistics['Standard Deviation'] = standard_deviation
statistics['Skewness'] = skewness
statistics['Kurtosis'] = kurtosis
print(statistics)


# In[143]:


import scipy.stats as stats
import math

sample_mean = 90.99
population_std_dev = 50.40
sample_size = 44
confidence_level = 0.95

#critical value (Z)
z_critical = stats.norm.ppf((1 + confidence_level) / 2)

# margin of error
margin_of_error = z_critical * (population_std_dev / math.sqrt(sample_size))

# confidence interval
lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print("Sample Mean:", sample_mean)
print("Sample size:", sample_size)
print("Population SD:", population_std_dev)
print("confidence level:", confidence_level)
print("Z-critical level:", z_critical)
print("Margin of error:", margin_of_error)
print("Z-critical level:", z_critical)
print(f"Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")


# In[118]:


import scipy.stats as stats

mean = 90.99
std_dev = 50.40

prob_a=stats.norm.cdf(50, loc=mean, scale=std_dev)
prob_b=1-stats.norm.cdf(75, loc=mean, scale=std_dev)
prob_c=stats.norm.cdf(100, loc=mean, scale=std_dev)-stats.norm.cdf(75, loc=mean, scale=std_dev)


print(f"a. p(x>50)={prob_a:.4f}")
print(f"b. p(x<100)={prob_b:.4f}")
print(f"c. p(50<x<100)={prob_c:.4f}")


# In[142]:



import random

# Sampling Technique
sampling_technique = "Random Sampling"


sample_size = 100
random.seed(42)

#sample data
sample = data.sample(sample_size)

# sample mean for 'ADR'
sample_mean_adr = sample['adr'].mean()

# population mean for 'ADR'
population_mean_adr = data['adr'].mean()


# Checking if the sample mean is similar to the population mean.
print("Sampling Technique Used:", sampling_technique)
print("Sample Mean for 'adr':", sample_mean_adr)
print("Population Mean for 'adr':", population_mean_adr)

