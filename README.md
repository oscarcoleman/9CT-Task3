# 9CT-Task3
## Thesis
From primary school to the end of high school, are students getting more or less proficient in literacy and mathematics, in Middle East, Central America, South America, Europe, Scandanavia, Oceania and Canada, comparatively?
## Functional and Non-Functional Requirements
### Functional
- Filters global_education.csv for grade_2_3_proficiency_reading, grade_2_3_proficiency_math, lower_secondary_end_proficiency_reading, lower_secondary_end_proficiency_math, youths_15_24_literacy_rates_male, and youths_15_24_literacy_rates_female columns
- Filters for the countries Argentina, Australia, Brazil, Canada, Chile, Colombia, Dominican Republic, Ecuador, Finland, France, Georgia, Germany, Guatemala, Qatar, Republic of Ireland, Mexico, Netherlands, New Zealand, Norway, Panama, Paraguay, Peru, Poland, Portugal, Saudi Arabia, Slovakia, Sweden, U.A.E, Vietnam
- Computes regional averages
- Visualise data in a bar graph, with primary school and high school data per country side-by-side, one red and one blue.
### Non-Functional
- Usability: GUI must allow simple interaction with data, "README" document oultines all aspects of the project, including thesis, requirements, code tests, and evaluation.
- Reliability: Data is cross-referenced and compared to various sources.
## Research
### SEE-I Paragraph
In some countries of the world, such as India, research indicates that school profiency is on the decline as students progress from primary school to the end of high school. As shown in a recent Indian government survey, relative student performace in both literacy and mathematics has been shown to fall by a few percentage points from Class 3 to Class 6 and Class 6 to 9. Most dramatically of all, however, it is to be seen that while 53% of Class 6 students knew times tables up to ten, only 28% could solve problems related to percentages by Class 9. On the whole, this is not a promising indication toward the effectiveness of continuous academic pursuits and deserves consideration.
### Source
https://www.hindustantimes.com/india-news/literacy-and-numeracy-proficiency-drop-as-students-progress-to-higher-classes-govt-survey-101752014255531.html 
## Code
### Raw CSV file

- ADD LINK

### Week 2 and Week 3
I developed the code for filtering rows and columns for desired countries:
#### Filter_columns.py
The following code removes the unnecessary columns from the raw file and moves them to a cleaned file "Global_Education_Cleaned.csv"
```
columns = [ 
           'Latitude ',
           'Longitude', 
           'OOSR_Pre0Primary_Age_Male', 
           'OOSR_Pre0Primary_Age_Female', 
           'OOSR_Primary_Age_Male', 
           'OOSR_Primary_Age_Female',
           'OOSR_Lower_Secondary_Age_Male',
           'OOSR_Lower_Secondary_Age_Female',
           'OOSR_Upper_Secondary_Age_Male',
           'OOSR_Upper_Secondary_Age_Female',
           'Completion_Rate_Primary_Male',
           'Completion_Rate_Primary_Female',
           'Completion_Rate_Lower_Secondary_Male',
           'Completion_Rate_Lower_Secondary_Female',
           'Completion_Rate_Upper_Secondary_Male',
           'Completion_Rate_Upper_Secondary_Female',
           'Birth_Rate',
           'Gross_Primary_Education_Enrollment',
           'Gross_Tertiary_Education_Enrollment',
           'Unemployment_Rate',
           'Youth_15_24_Literacy_Rate_Male',
           'Youth_15_24_Literacy_Rate_Female'
]

df = df.drop(columns=columns)

df.to_csv('Global_Education_Cleaned.csv', index=False)
```
#### Filter_rows.py
The following code selects the rows for the desired countries and move them to a new file "Global_Ed_Cleaned2.csv", which will be used for final analysis.
```
df = pd.read_csv("Global_Education_Cleaned.csv", encoding='ISO-8859-1')

rows = [7, 9, 24, 33, 36, 37, 38, 50, 53, 54, 63, 64, 67, 68, 72, 85, 114, 126, 127, 133, 137, 139, 142, 143, 162, 173, 198]

df = df.iloc[rows, :]

df.to_csv("Global_Ed_Cleaned2.csv", index=False)
```
### Week 3 Continued
#### Visualisations.py
##### Individual Country Display
The following code is for the display of data concerning Europe. I, as can be seen in visualisations.py, have done the same for each region with the specific details, particularly the rows, changed as per the region:
```
# ----- EUROPE LITERACY

rows_eu = [10, 12, 14, 16, 22, 23, 26] 

values1_eu = df.iloc[rows_eu, 1] 
values2_eu = df.iloc[rows_eu, 3]
values3_eu = df.iloc[rows_eu, 5]

labels = df.iloc[rows_eu, 0].tolist()
labels_shifted = labels[:1] + labels[1:]


x = np.arange(len(labels_shifted)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(x - width, values1_eu, width, label='Mid-Primary School')
ax.bar(x, values2_eu, width, label='End-Primary School')
ax.bar(x + width, values3_eu, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels_shifted, rotation=45, ha='right')
ax.set_ylabel('Score')
ax.set_title('Europe Student Literacy Performance')
ax.legend()
plt.savefig('eu_literacy.png')

# ----- EUROPE MATH

values4_eu = df.iloc[rows_eu, 2] 
values5_eu = df.iloc[rows_eu, 4]
values6_eu = df.iloc[rows_eu, 6]

x = np.arange(len(labels_shifted)) 
width = 0.2

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(x - width, values4_eu, width, label='Mid-Primary School')
ax.bar(x, values5_eu, width, label='End-Primary School')
ax.bar(x + width, values6_eu, width, label='End-High School')

ax.set_xticks(x)
ax.set_xticklabels(labels_shifted, rotation=45, ha='right')
ax.set_ylabel('Score')
ax.set_title('Europe Student Math Performance')
ax.legend()
plt.savefig('eu_math.png')
```
Explanation:
- rows_eu: list of indeces from Global_Ed_Cleaned2.csv that consists of each country being researched and their accompanying data
- values1_eu (as well as 2, 3, 4, 5, 6): finds specific data from column, e.g of primary school math or high school literacy.
- The first block of code below is as in the more complete above code, however it is specific to such. The second attached code below is regular for the rest of visualisations.py. The code was changed for the European data due to a problem in linking the values data and the labels data, namely that the label was ascribed to an index one greater than desirable.
```
labels = df.iloc[rows_eu, 0].tolist()
labels_shifted = labels[:1] + labels[1:]
```

```
labels = df.iloc[rows_ca, 0].tolist()
```
##### Avg regional scores
The following code is again specific to the European data, but is only slightly tweaked for the rest of the countries. Its aim is to find a set of average scores for each region which can later be used to represent that region in the world data:
```
# EUROPE
total_values1_eu = values1_eu.sum()
country_count = len(rows_ca)
avg_total_values1_eu = total_values1_eu / country_count

total_values2_eu = values2_eu.sum()
country_count = len(rows_ca)
avg_total_values2_eu = total_values2_eu / country_count

total_values3_eu = values3_eu.sum()
country_count = len(rows_ca)
avg_total_values3_eu = total_values3_eu / country_count

total_values4_eu = values4_eu.sum()
country_count = len(rows_ca)
avg_total_values4_eu = total_values4_eu / country_count

total_values5_eu = values5_eu.sum()
country_count = len(rows_ca)
avg_total_values5_eu = total_values5_eu / country_count

total_values6_eu = values6_eu.sum()
country_count = len(rows_ca)
avg_total_values6_eu = total_values6_eu / country_count
```
- values.sum creates a sum of all scores within country
- country count is equal to the total number of indeces within each set of rows
- avg = sum / n of rows
## EXPLAIN SCORE MEANING
