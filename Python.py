import pandas as pd 
df=pd.read_csv('customer_shopping_behavior.csv')    #reading the file
print(df.head())                                    #printing first 5 rows
print(df.info())   #printing the description of data                              
print(df.describe())        #prints the summary of statistics columns(only numerical)
print(df.describe(include='all'))     #prints the summary of all the columns(non statistical too)
print(df.isnull().sum())          #printing the sum of the no. of null values
df['Review Rating']=df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median())) 
#we update the null values with the 'median' of each 'category'
print(df.isnull().sum())        #check again
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(' ','_')
print(df.columns)