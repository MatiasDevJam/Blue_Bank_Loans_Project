import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# method 1 to read json

json_file = open('./data/loan_data_json.json')
data = json.load(json_file)

# method 2 to read json

with open('./data/loan_data_json.json') as json_file:
    data = json.load(json_file)

data_df = pd.DataFrame(data)

# finding unique values for the purpose column
data_df['purpose'].unique()

data_df.describe()

# using exp() to get annual income
income = np.exp(data_df['log.annual.inc'])
data_df['annualincome'] = income 

# FICO score

# applying for loops to loan data

length = len(data_df)
ficocat = []
for x in range(0, length):
    category = data_df['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 700:
            cat = 'Good'
        elif category >= 700:
            cat = 'Excellent'
        else:
            cat = 'Unknown'
    except:
        cat = 'Unknown'
        
    ficocat.append(cat)
    
ficocat = pd.Series(ficocat)

data_df['fico.category'] = ficocat

# df.loc as conditional statements

data_df.loc[data_df['int.rate'] > 0.12, 'int.rate.type'] = 'High'
data_df.loc[data_df['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

# number of loans/rows br fico.category

catplot = data_df.groupby(['fico.category']).size()
catplot.plot.bar(color = 'red', width = 0.2)
plt.show()

purposecount = data_df.groupby(['purpose']).size()
purposecount.plot.bar(color = 'black', width = 0.2)
plt.show()

# scatter plots

ypoint = data_df['annualincome']
xpoint = data_df['dti']
plt.scatter(xpoint, ypoint, color = 'blue')
plt.show()

data_df.to_csv('./data/data_cleaned.csv', index= True)