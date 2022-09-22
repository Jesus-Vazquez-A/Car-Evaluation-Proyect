#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings


# In[2]:


warnings.filterwarnings("ignore")


# In[3]:


url = "C:\\Users\\PC\\Desktop\\Ciencias de datos\\Proyectos\\Car Evaluation\\data\\Car_Evaluation_Preprocessing.csv"
df=pd.read_csv(url)


# In[4]:


sns.set_style(style="whitegrid")


# In[5]:


sns.countplot(data=df,x="class",palette="Set2")
plt.show()


# There is a clear imbalance between classes. Therefore, it is advisable to treat the data.

# In[6]:


def load_inputs_outputs():
    
    return df.drop(["class"],axis="columns"),df["class"]

X,y=load_inputs_outputs()


# In[7]:


from imblearn.over_sampling import SMOTE


# In[8]:


smote=SMOTE()


# In[9]:


X_balanced,y_balanced=smote.fit_resample(X,y)


# In[10]:


df_balanced=pd.concat([X_balanced,y_balanced],axis="columns")


# In[24]:


fig,(ax,ax1)= plt.subplots(1,2,figsize = (20,8))
ax.set_title("Imbalanced Dataset")
sns.countplot(data=df,x="class",palette="Set2",ax=ax)
ax1.set_title("Balanced Dataset")
sns.countplot(data=df_balanced,x="class",palette="Set2",ax=ax1)
plt.savefig( "C:\\Users\\PC\\Desktop\\Ciencias de datos\\Proyectos\\Car Evaluation\\img\\SMOTE.png")
plt.show()


# In[25]:


url = "C:\\Users\\PC\\Desktop\\Ciencias de datos\\Proyectos\\Car Evaluation\\data\\Car_Evaluation_Balanced.csv"
df_balanced.to_csv(url,index=False)

