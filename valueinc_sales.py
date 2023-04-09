import pandas as pd
df=pd.read_csv('G:/GetFreeCourses.Co-Udemy-Python and Tableau The Complete Data Analytics Bootcamp!/3. Python - Project 1 Value Inc. Sales Analysis/transaction.csv',sep=';')
df.head()
df.tail()
df.info()
df.describe()
df.columns
#Defining Variables
CostPerItem = df['CostPerItem']
NumberOfItemsPurchased=df['NumberOfItemsPurchased']
CostPerTransaction=CostPerItem*NumberOfItemsPurchased
CostPerTransaction
#adding a new column to the dataframe
df['CostPerTransaction']=CostPerTransaction
df.info()
df['SalesPerTransaction']=df['SellingPricePerItem']*df['NumberOfItemsPurchased']
df.info()
df['ProfitPerTransaction']=df['SalesPerTransaction']-df['CostPerTransaction']
df.info()
df['Markup']=df['ProfitPerTransaction']/df['CostPerTransaction']
df['Markup']=round(df['Markup'],2)
df['date']=df['Day'].astype(str)+'-'+df['Month']+'-'+df['Year'].astype(str)
df.info()
df.iloc[0]
df.iloc[0:3]
df.iloc[-5:]
df.iloc[:,3]#all rows and 4th column(as its zero-indexed)
df.iloc[:,0]
df.head()
split_col=df['ClientKeywords'].str.split(',',expand=True)
df['ClientAge']=split_col[0]
df['ClientType']=split_col[1]
df['LengthofContract']=split_col[2]
df['ClientAge']=df['ClientAge'].str.replace('[','')
df['LengthofContract']=df['LengthofContract'].str.replace('[','')
df['ItemDescription']=df['ItemDescription'].str.lower()
seasons=pd.read_csv('value_inc_seasons.csv',sep=';')
df=pd.merge(df,seasons, on='Month')
df=df.drop('ClientKeywords',axis=1)
df=df.drop('Day',axis=1)
df=df.drop(['Year','Month'],axis=1)
df.to_csv('ValueInc_Cleaned.csv',index=False)
