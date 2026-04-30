
# coding: utf-8

# In[1]:


import pandas as pd

# Load dataset
df = pd.read_csv('Student_data.csv')

# Display first 5 rows
df.head()


# In[2]:


print(df.info())
print(df.describe())


# In[3]:


df.columns = df.columns.str.strip()
print(df.columns)


# In[4]:


print(df.isnull().sum())


# In[5]:


# Fill numerical missing values with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Verify
print(df.isnull().sum())


# In[6]:


df_encoded = pd.get_dummies(df, drop_first=True)

# Display result
df_encoded.head()


# In[7]:


print("Duplicates:", df_encoded.duplicated().sum())


# In[12]:


df_encoded.to_csv('student_prepared.csv', index=False)
print("SUCCESS: Data cleaned, encoded, and saved!")

