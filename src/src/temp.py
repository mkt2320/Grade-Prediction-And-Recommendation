

import pandas as pd
import random

# Define column names
columns = ['student_id', 'age', 'Medu', 'Fedu', 'traveltime', 'studytime', 'failures', 'famrel',
           'freetime', 'goout', 'Dalc', 'Walc', 'health', 'absences', 'G1', 'G2',
           'school_MS', 'sex_M', 'address_U', 'famsize_LE3', 'Pstatus_T',
           'Mjob_health', 'Mjob_other', 'Mjob_services', 'Mjob_teacher',
           'Fjob_health', 'Fjob_other', 'Fjob_services', 'Fjob_teacher',
           'reason_home', 'reason_other', 'reason_reputation', 'guardian_mother',
           'guardian_other', 'schoolsup_yes', 'famsup_yes', 'paid_yes',
           'activities_yes', 'nursery_yes', 'higher_yes', 'internet_yes',
           'romantic_yes']

# Generate random data for each column
data = []
for i in range(10):
    row_data = {'student_id': 1000+i}
    # Age: Numeric value from 15 to 22
    row_data['age'] = random.randint(15, 22)
    # Mother's and father's education: Numeric value from 0 to 4
    row_data['Medu'] = random.randint(0, 4)
    row_data['Fedu'] = random.randint(0, 4)
    # Travel time: Categorical values 1 to 4
    row_data['traveltime'] = random.randint(1, 4)
    # Weekly study time: Categorical values 1 to 4
    row_data['studytime'] = random.randint(1, 4)
    # Failures: Numeric value from 0 to 3, or 3 if greater than 3
    row_data['failures'] = min(random.randint(0, 3), 3)
    # Quality of family relationships: Numeric value from 1 to 5
    row_data['famrel'] = random.randint(1, 5)
    # Free time after school: Numeric value from 1 to 5
    row_data['freetime'] = random.randint(1, 5)
    # Going out with friends: Numeric value from 1 to 5
    row_data['goout'] = random.randint(1, 5)
    # Workday alcohol consumption: Numeric value from 1 to 5
    row_data['Dalc'] = random.randint(1, 5)
    # Weekend alcohol consumption: Numeric value from 1 to 5
    row_data['Walc'] = random.randint(1, 5)
    # Current health status: Numeric value from 1 to 5
    row_data['health'] = random.randint(1, 5)
    # Number of school absences: Numeric value from 0 to 93
    row_data['absences'] = random.randint(0, 93)
    # First and second period grades: Numeric value from 0 to 20
    row_data['G1'] = random.randint(0, 20)
    row_data['G2'] = random.randint(0, 20)
    # Categorical variables: Assigning random values of 0 or 1
    for col in columns[16:]:
        row_data[col] = random.choice([0, 1])
    print(row_data)
    data.append(row_data)
    
df = pd.DataFrame(data)
df.to_csv("test_dataset.csv", index=False)
