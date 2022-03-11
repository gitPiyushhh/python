####################################################
######## Using Dictionaries🙂

my_dict = {
    'name': 'Piyush',
    'age': 21,
    'profession': 'Developer'
}

#### 1️⃣ Logging of values #####
print(my_dict, type(my_dict))

print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('name'))

#### 2️⃣ Iterating through for loop #####

for i in my_dict:
    print(i)

for i in my_dict.values():
    print(i)

#### 3️⃣ Updation of values #####

my_dict['name'] = 'Jonas'
my_dict['lvl'] = 'Expert'


#### 4️⃣ Deletion of values #####

my_dict.pop('lvl')
print(my_dict)

## Using DEL fctn
del my_dict['age']

#################################################
######### NESTED DICTIONARIES😌

emp_details = {
    'Employees': {
        'Piyush': {'id': 1, 'salary': 1000},
        'Jonas': {'id': 2, 'salary': 5000}
    }
}

print(emp_details)


###################################################
############ CONVERTING TO DATA_FRAMES😏

import pandas as pd

df = pd.DataFrame(emp_details['Employees'])

print(df)