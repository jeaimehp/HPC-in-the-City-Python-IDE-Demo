#!/usr/bin/env python
# coding: utf-8

# # HPC in the City Jupyter Training
# 
# **Purpose**
# 
# This notebook was created to display some python basics using the Jupyter Platform
# 
# ----
# 
# ## Using the requests module to download a dataset file
# 

# In[2]:


import requests

# Data Source: DataAtlanta - http://hackhpc.org/data/#local
url = 'https://nwis.waterdata.usgs.gov/nwis/uv?cb_00010=on&cb_00060=on&cb_00065=on&cb_00095=on&cb_00300=on&cb_00400=on&cb_63680=on&format=rdb&site_no=02336240&period=&begin_date=2020-01-01&end_date=2020-10-07'


# In[58]:


# Downloads the web request using the provided url
r = requests.get(url)

# Writes out the request as a tab seperated value (tsv) file 
with open('atl-water-data.tsv', 'wb') as f:
    f.write(r.content)


# In[40]:


# Import the os library to list the files in the current directory
import os
print (os.listdir())


# In[42]:


# Preview the first few lines of the dataset file
N = 45
with open("atl-water-data.tsv") as myfile:
    head = [next(myfile) for x in range(N)]
for l in head:
    print(l, end='')


# # Saving the dataset as a DataFrame

# In[51]:


# Import the tsv into a dataframe in Pandas
import pandas as pd

atlwaterDF = pd.read_csv('atl-water-data.tsv', sep='\t', header=35)
atlwaterDF = atlwaterDF.drop([0])
atlwaterDF.head()


# # Header information provided by the downloaded file
# 
# Data for the following 1 site(s) are contained in this file
#  USGS 02336240 S.F. PEACHTREE CREEK JOHNSON RD, NEAR ATLANTA, GA
# 
# -----------------------------------------------------------------------------------
# 
#  Data provided for site 02336240
#  
#  
# |    TS |  parameter  |   Description                                             |
# |-------|-------------|-----------------------------------------------------------|
# |39623  |     00065   |  Gage height, feet                                        |
# |39624  |     00060   |  Discharge, cubic feet per second                         |
# |39626  |     00010   |  Temperature, water, degrees Celsius                      |
# |39627  |     00095   |  Specific conductance, water, unfiltered                  |
# |39628  |     00300   |  Dissolved oxygen, water, unfiltered, milligrams per liter|
# |39629  |     00400   |  pH, water, unfiltered, field, standard units             |
# | 39630 |      63680  |   Turbidity, water, unfiltered                            |
#         

# # Dataframe basic statisical analysis
# 
# The .describe() method can be used to show general information regarding a large dataset.

# In[43]:


atlwaterDF.describe()


# # Plot one of the datasets
# 
# In the below graph we could be looking at Dissolve Oxygen (39628_00300	Dissolved oxygen) as a metric for water quality health from January - October 2020
# 

# In[57]:


# matplotlib library needed to produce plots
import matplotlib.pyplot as plt
plt.close('all')
plt.figure()
#Using the dataframe with the dataset, defining the needed column, 
#converting the datatype from string into numbers and then ploting the results



# To see the figure the Pandas plot was adjusted to add .get_figure and then
# Save it out to an actual picture.
fig = atlwaterDF['39628_00300'].apply(pd.to_numeric).plot().get_figure()

fig.savefig('plot.png')


# In[ ]:




