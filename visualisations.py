# display bar graph for each region, with each country showing their primary and high school scores side-by-side
# display world bar graph that compares the regional averages

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Global_Ed_Cleaned2.csv', encoding='ISO-8859-1') # creates dataframe for file to be used, has already been cleaned


# ----- SCANDANAVIA LITERACY 

rows_scan = [6, 9, 18, 27] # contains indeces from dataframe in which Scandanavian data will be found

values1_scan = df.iloc[rows_scan, 1] # selects column for mid-primary literacy
values2_scan = df.iloc[rows_scan, 5] # selects column for end-high literacy

labels = df.iloc[rows_scan, 0].tolist() # string value from first column (country name) added to list

x = np.arange(len(labels))  
width = 0.35  # width of the bars

fig, ax = plt.subplots()

# creates bars per country
ax.bar(x - width/2, values1_scan, width, label='Mid-Primary School')
ax.bar(x + width/2, values2_scan, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Scandanavia Student Literary Performance')
ax.legend()
plt.savefig('scan_literacy.png')

# ----- SCANDANAVIA MATH 

values3_scan = df.iloc[rows_scan, 2] # selects column for mid-primary math
values4_scan = df.iloc[rows_scan, 6] # selects column for end-high math

x = np.arange(len(labels)) 
width = 0.35  # width of the bars

fig, ax = plt.subplots()
ax.bar(x - width/2, values3_scan, width, label='Mid-Primary School')
ax.bar(x + width/2, values4_scan, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Scandanavia Student Math Performance')
ax.legend()
plt.savefig('scan_math.png')

# ----- EUROPE LITERACY

rows_eu = [10, 12, 14, 16, 22, 23, 26] # contains indeces from dataframe in which European data will be found

values1_eu = df.iloc[rows_eu, 1] # selects column for mid-primary literacy
values2_eu = df.iloc[rows_eu, 3] # selects column for end-primary literacy
values3_eu = df.iloc[rows_eu, 5] # selects column for end-high literacy

labels = df.iloc[rows_eu, 0].tolist() # string value from first column (country name) added to list
labels_shifted = labels[:1] + labels[1:] # label values and indeces misaligned, ie each is shifted over to the next value in order

x = np.arange(len(labels_shifted)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width, values1_eu, width, label='Mid-Primary School')
ax.bar(x, values2_eu, width, label='End-Primary School')
ax.bar(x + width, values3_eu, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels_shifted, rotation=45, ha='right')
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Europe Student Literacy Performance')
ax.legend()
plt.savefig('eu_literacy.png')

# ----- EUROPE MATH

values4_eu = df.iloc[rows_eu, 2] # selects column for mid-primary math
values5_eu = df.iloc[rows_eu, 4] # selects column for end-primary math
values6_eu = df.iloc[rows_eu, 6] # selects column for end-high math

x = np.arange(len(labels_shifted)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width, values4_eu, width, label='Mid-Primary School')
ax.bar(x, values5_eu, width, label='End-Primary School')
ax.bar(x + width, values6_eu, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels_shifted, rotation=45, ha='right')
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Europe Student Math Performance')
ax.legend()
plt.savefig('eu_math.png')

# ----- CENTRAL AMERICA LITERACY 

rows_ca = [7, 13, 15, 19] # contains indeces from dataframe in which Central American data will be found

values1_ca = df.iloc[rows_ca, 1] # selects column for mid-primary literacy
values2_ca = df.iloc[rows_ca, 3] # selects column for end-primary literacy
values3_ca = df.iloc[rows_ca, 5] # selects column for end-high literacy

labels = df.iloc[rows_ca, 0].tolist() # string value from first column (country name) added to list

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width, values1_ca, width, label='Mid-Primary School')
ax.bar(x, values2_ca, width, label='End-Primary School')
ax.bar(x + width, values3_ca, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Central America and Carribeans Student Literacy Performance')
ax.legend()
plt.savefig('ca_literacy.png')

# ----- CENTRAL AMERICA MATH 

values4_ca = df.iloc[rows_ca, 2] # selects column for mid-primary math
values5_ca = df.iloc[rows_ca, 4] # selects column for end-primary math
values6_ca = df.iloc[rows_ca, 6] # selects column for end-high math

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width, values4_ca, width, label='Mid-Primary School')
ax.bar(x, values5_ca, width, label='End-Primary School')
ax.bar(x + width, values6_ca, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Central America and Carribeans Student Math Performance')
ax.legend()
plt.savefig('ca_math.png')

# ----- SOUTH AMERICA LITERACY 

rows_sa = [0, 2, 4, 5, 8, 20, 21] # contains indeces from dataframe in which South American data will be found

values1_sa = df.iloc[rows_sa, 1] # selects column for mid-primary literacy
values2_sa = df.iloc[rows_sa, 3] # selects column for end-primary math
values3_sa = df.iloc[rows_sa, 5] # selects column for end-high literacy

labels = df.iloc[rows_sa, 0].tolist() # string value from first column (country name) added to list

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width, values1_sa, width, label='Mid-Primary School')
ax.bar(x, values2_sa, width, label='End-Primary School')
ax.bar(x + width, values3_sa, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('South America Student Literacy Performance')
ax.legend()
plt.savefig('sa_literacy.png')

# ----- SOUTH AMERICA MATH 

values4_sa = df.iloc[rows_sa, 2] # selects column for mid-primary math
values5_sa = df.iloc[rows_sa, 4] # selects column for end-primary math
values6_sa = df.iloc[rows_sa, 6] # selects column for end-high math

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width, values4_sa, width, label='Mid-Primary School')
ax.bar(x, values5_sa, width, label='End-Primary School')
ax.bar(x + width, values6_sa, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('South America Student Math Performance')
ax.legend()
plt.savefig('sa_math.png')

# ----- MIDDLE EAST LITERACY 

rows_me = [11, 24, 25, 28] # contains indeces from dataframe in which Middle Eastern data will be found

values1_me = df.iloc[rows_me, 1] # selects column for mid-primary literacy
values2_me = df.iloc[rows_me, 5] # selects column for end-high literacy

labels = df.iloc[rows_me, 0].tolist() # string value from first column (country name) added to list

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width / 2, values1_me, width, label='Mid-Primary School')
ax.bar(x + width / 2, values2_me, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Middle East Student Literacy Performance')
ax.legend()
plt.savefig('me_literacy.png')

# ----- MIDDLE EAST MATH 

values3_me = df.iloc[rows_me, 2] # selects column for mid-primary math
values4_me = df.iloc[rows_me, 6] # selects column for end-high math

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width / 2, values3_me, width, label='Mid-Primary School')
ax.bar(x + width / 2, values4_me, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Middle East Student Math Performance')
ax.legend()
plt.savefig('me_math.png')

# ----- OCEANIA LITERACY 

rows_oc = [1, 17] # contains indeces from dataframe in which Oceanic data will be found

values1_oc = df.iloc[rows_oc, 1] # selects column for mid-primary literacy
values2_oc = df.iloc[rows_oc, 5] # selects column for end-high literacy

labels = df.iloc[rows_oc, 0].tolist() # string value from first column (country name) added to list

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width / 2, values1_oc, width, label='Mid-Primary School')
ax.bar(x + width / 2, values2_oc, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Oceania Student Literacy Performance')
ax.legend()
plt.savefig('oc_literacy.png')

# ----- OCEANIA MATH 

values3_oc = df.iloc[rows_oc, 2] # selects column for mid-primary math
values4_oc = df.iloc[rows_oc, 6] # selects column for end-high math

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width / 2, values3_oc, width, label='Mid-Primary School')
ax.bar(x + width / 2, values4_oc, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('Oceania Student Math Performance')
ax.legend()
plt.savefig('oc_math.png')

# ----- CANADA LITERACY
rows_can = [3] # contains indeces from dataframe in which Canadian data will be found

values1_can = df.iloc[rows_can, 1].iloc[0]  # selects column for mid-primary literacy
values2_can = df.iloc[rows_can, 5].iloc[0]  # selects column for end-high literacy

# ----- CANADA MATH
values3_can = df.iloc[rows_can, 2].iloc[0] # selects column for mid-primary math
values4_can = df.iloc[rows_can, 6].iloc[0]  # selects column for end-high literacy

# ------ AVG REGIONAL SCORES 

# SCANDANAVIA
values1_scan_clean = values1_scan.replace(0, np.nan) # replaces '0' values with 'nan'
avg_total_values1_scan = values1_scan_clean.mean(skipna=True) # cleans out 'nan' values and computes an avg

values2_scan_clean = values2_scan.replace(0, np.nan)
avg_total_values2_scan = values2_scan_clean.mean(skipna=True)

values3_scan_clean = values3_scan.replace(0, np.nan)
avg_total_values3_scan = values3_scan_clean.mean(skipna=True)

values4_scan_clean = values4_scan.replace(0, np.nan)
avg_total_values4_scan = values4_scan_clean.mean(skipna=True)

# EUROPE

values1_eu_clean = values1_eu.replace(0, np.nan)
avg_total_values1_eu = values1_eu_clean.mean(skipna=True)

values2_eu_clean = values2_eu.replace(0, np.nan)
avg_total_values2_eu = values2_eu_clean.mean(skipna=True)

values3_eu_clean = values3_eu.replace(0, np.nan)
avg_total_values3_eu = values3_eu_clean.mean(skipna=True)

values4_eu_clean = values4_eu.replace(0, np.nan)
avg_total_values4_eu = values4_eu_clean.mean(skipna=True)

values5_eu_clean = values5_eu.replace(0, np.nan)
avg_total_values5_eu = values5_eu_clean.mean(skipna=True)

values6_eu_clean = values6_eu.replace(0, np.nan)
avg_total_values6_eu = values6_eu_clean.mean(skipna=True)

# CENTRAL AMERICA
values1_ca_clean = values1_ca.replace(0, np.nan)
avg_total_values1_ca = values1_ca_clean.mean(skipna=True)

values2_ca_clean = values2_ca.replace(0, np.nan)
avg_total_values2_ca = values2_ca_clean.mean(skipna=True)

values3_ca_clean = values3_ca.replace(0, np.nan)
avg_total_values3_ca = values3_ca_clean.mean(skipna=True)

values4_ca_clean = values4_ca.replace(0, np.nan)
avg_total_values4_ca = values4_ca_clean.mean(skipna=True)

values5_ca_clean = values5_ca.replace(0, np.nan)
avg_total_values5_ca = values5_ca_clean.mean(skipna=True)

values6_ca_clean = values6_ca.replace(0, np.nan)
avg_total_values6_ca = values6_ca_clean.mean(skipna=True)

# SOUTH AMERICA
values1_sa_clean = values1_sa.replace(0, np.nan)
avg_total_values1_sa = values1_sa_clean.mean(skipna=True)

values2_sa_clean = values2_sa.replace(0, np.nan)
avg_total_values2_sa = values2_sa_clean.mean(skipna=True)

values3_sa_clean = values3_sa.replace(0, np.nan)
avg_total_values3_sa = values3_sa_clean.mean(skipna=True)

values4_sa_clean = values4_sa.replace(0, np.nan)
avg_total_values4_sa = values4_sa_clean.mean(skipna=True)

values5_sa_clean = values5_sa.replace(0, np.nan)
avg_total_values5_sa = values5_sa_clean.mean(skipna=True)

values6_sa_clean = values6_sa.replace(0, np.nan)
avg_total_values6_sa = values6_sa_clean.mean(skipna=True)

# MIDDLE EAST
values1_me_clean = values1_me.replace(0, np.nan)
avg_total_values1_me = values1_me_clean.mean(skipna=True)

values2_me_clean = values2_me.replace(0, np.nan)
avg_total_values2_me = values2_me_clean.mean(skipna=True)

values3_me_clean = values3_me.replace(0, np.nan)
avg_total_values3_me = values3_me_clean.mean(skipna=True)

values4_me_clean = values4_me.replace(0, np.nan)
avg_total_values4_me = values4_me_clean.mean(skipna=True)

# OCEANIA
values1_oc_clean = values1_oc.replace(0, np.nan)
avg_total_values1_oc = values1_oc_clean.mean(skipna=True)

values2_oc_clean = values2_oc.replace(0, np.nan)
avg_total_values2_oc = values2_oc_clean.mean(skipna=True)

values3_oc_clean = values3_oc.replace(0, np.nan)
avg_total_values3_oc = values3_oc_clean.mean(skipna=True)

values4_oc_clean = values4_oc.replace(0, np.nan)
avg_total_values4_oc = values4_oc_clean.mean(skipna=True)

# ----- WORLD LITERACY 

# each list of the below likeness contains regional avg values for mid-primary, end-primary and end-high school math and literacy respectively
values1_w = [
    avg_total_values1_scan,  
    avg_total_values1_eu,    
    avg_total_values1_ca,    
    avg_total_values1_sa,    
    avg_total_values1_me,    
    avg_total_values1_oc,
    values1_can             
] 

values2_w = [
    np.nan,                  
    avg_total_values2_eu,    
    avg_total_values2_ca,    
    avg_total_values2_sa,    
    np.nan,                  
    np.nan,                  
    np.nan                  
] 

values3_w = [
    avg_total_values2_scan,  
    avg_total_values3_eu,    
    avg_total_values3_ca,    
    avg_total_values3_sa,    
    avg_total_values2_me,    
    avg_total_values2_oc,    
    values2_can              
] 

with open("regions.txt", "r") as txt_file: # opens txt file w/ list of regions
    lines = txt_file.readlines()

labels = lines[:7] # country names turned to labels

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per region
ax.bar(x - width, values1_w, width, label='Mid-Primary School')
ax.bar(x, values2_w, width, label='End-Primary School')
ax.bar(x + width, values3_w, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('World Student Literacy Performance')
ax.legend()
plt.savefig('world_literacy.png')
plt.show()


# ----- WORLD MATH 

values4_w = [
    avg_total_values3_scan,  
    avg_total_values4_eu,
    avg_total_values4_ca,    
    avg_total_values4_sa,   
    avg_total_values4_me,    
    avg_total_values4_oc,   
    values3_can             
] 

values5_w = [
    np.nan,                 
    avg_total_values5_eu,    
    avg_total_values5_ca,    
    avg_total_values5_sa,   
    np.nan,                 
    np.nan,                  
    np.nan                  
] 

values6_w = [
    avg_total_values4_scan,  
    avg_total_values6_eu,
    avg_total_values6_ca,    
    avg_total_values6_sa,    
    avg_total_values4_me,   
    avg_total_values4_oc,   
    values4_can             
] 

x = np.arange(len(labels)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

# creates bars per country
ax.bar(x - width, values4_w, width, label='Mid-Primary School')
ax.bar(x, values5_w, width, label='End-Primary School')
ax.bar(x + width, values6_w, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.set_ylabel('Score (% of students meeting basic profiency)')
ax.set_title('World Student Math Performance')
ax.legend()
plt.savefig('world_math.png')
plt.show()
