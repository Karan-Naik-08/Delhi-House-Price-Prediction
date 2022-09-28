import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('MagicBricks.csv')

df['Bathroom']=df['Bathroom'].fillna(2)
df['Parking']=df['Parking'].fillna(2)
df['Furnishing']=df['Furnishing'].fillna('Semi-Furnished')
df['Type']=df['Type'].fillna('Apartment')

sq_mean= df['Per_Sqft'].mean()
df['Per_Sqft']=df['Per_Sqft'].fillna(sq_mean)

df=df[
      (df.BHK <= 6)
     & (df.Bathroom<=6)
     & (df.Area<=11000)
    
]

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

df['Furnishing']=le.fit_transform(df['Furnishing'])
df['Type']=le.fit_transform(df['Type'])
df['Transaction']=le.fit_transform(df['Transaction'])
df['Status']=le.fit_transform(df['Status'])

df['Bathroom']= df['Bathroom'].astype(int)
df['Parking']= df['Parking'].astype(int)
df['Area']= df['Area'].astype(int)

x=df.drop([ 'Locality','Price','Per_Sqft' ],axis=1)
y=df['Price']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from num2words import num2words 


LR=LinearRegression()

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=1)

LR.fit(x_train,y_train)

pred=LR.predict(x_test)
error=r2_score(y_test,pred)
print(error)

inpt=np.array([['800','3','2','1','2','1','0','1']])

def give_pred(inpt):
    inpt=inpt.astype(int)
    predictin=int(LR.predict(inpt))
    in_words=num2words(predictin,lang='en_IN')
    return in_words

#print(give_pred(inpt))