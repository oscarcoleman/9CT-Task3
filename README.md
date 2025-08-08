# 9CT-Task3
## Thesis
From primary school to the end of high school, are students getting more or less proficient in literacy and mathematics, in Eastern Asia, Central America, South America, Europe, Scandanavia, Oceania and Canada, comparatively?
## Functional and Non-Functional Requirements
### Functional
- Filters global_education.csv for grade_2_3_proficiency_reading, grade_2_3_proficiency_math, lower_secondary_end_proficiency_reading, lower_secondary_end_proficiency_math, youths_15_24_literacy_rates_male, and youths_15_24_literacy_rates_female columns
- Filters for the countries Argentina, Australia, Brazil, Canada, Chile, China, Colombia, Dominican Republic, Ecuador, Finland, France, Georgia, Germany, Guatemala, Republic of Ireland, Mexico, Netherlands, New Zealand, Norway, Panama, Paraguay, Poland, Portugal, Slovakia, Sweden, Vietnam
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
#### Visualisation.py
- PROVIDE CODE AND EXPLAIN:
```
labels = df.iloc[rows_eu, 0].tolist()
labels_shifted = labels[:1] + labels[1:]
```
## EXPLAIN SCORE MEANING
