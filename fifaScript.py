    #Cleaning excercice for the dataset from FIFA
    #Link: https://www.kaggle.com/datasets/yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring

import pandas as pd
from datetime import datetime, timedelta

df = pd.read_csv(r"C:\Users\Pedro\Documents\PythonScripts\fifa21_raw_data.csv")


    #Show all the columns#
pd.set_option('display.max_columns', None)

    #Convert the height and weight columns to numerical forms

    #Change 'Height' column to an int data type

#df['Height'] = df['Height'].astype(int)

    # but it will throw error because some data contains non-numeric characters (such as single quote and double quote),
    # so it cannot be converted directly to an integer.

dataTypesAnalysis = df.dtypes

print(dataTypesAnalysis)

print(df["Height"].dtype)


df['Height']=df['Height'].str.replace("'","")

df['Height']=df['Height'].str.replace('"','')

df['Height']=df['Height'].astype(int)

print(df["Height"].dtype)

    #Lo mismo con weight
df['Weight']=df['Weight'].str.replace('lbs','')

df['Weight']=df['Weight'].astype(int)

#####Remove the unnecessary newline characters from all columns that have them.

    #Clean the 'Team & Contract' column, a lot of '\n'

df['Team & Contract']=df['Team & Contract'].str.replace("\n", "")


    # Based on the 'Joined' column, check which players have been playing at a club for more than 10 years
print(df['Joined'].dtype)

df['Joined'] = pd.to_datetime(df['Joined'], format='%b %d, %Y')

print(df['Joined'].dtype)

actual_date = datetime.now()

limit_date= actual_date - timedelta(days=365*10)

df_filter_newplayers = df[df['Joined']<limit_date]

    #'Value', 'Wage' and "Release Clause' are string columns. Convert them to numbers.
    # For eg, "M" in value column is Million, so multiply the row values by 1,000,000, etc.

columns_to_int = ['Value', 'Wage', 'Release Clause']
for column in columns_to_int:
    df[column] = df[column].replace('[\€,M]','',regex=True).astype(float)*1e6
    df[column] = df[column].replace('[\€,K]','',regex=True).astype(float)*1e3
    df[column] = df[column].astype(int)

    #Some columns have 'star' characters. Strip those columns of these stars and make the columns numerical
    
columns_to_int_star = ['W/F', 'SM', 'IR']
for column in columns_to_int_star:
    df[column] = df[column].str.replace('★','')
    df[column] = df[column].astype(int)

    #Which players are highly valuable but still underpaid (on low wages)? (hint: scatter plot between wage and value)

df['simple_correlation'] = df['Value'] / df['Wage']

    #Its sort the information with the height values at the top

df_order_sc = df.sort_values(by='scatter_plot', ascending=False) 

    #Filter all the rows that have Value and Wage equal to cero

df = df[(df['Value'] != 0) | (df['Wage'] != 0)]







