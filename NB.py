import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


import pickle
dataset=pd.read_csv("C:\\Users\\Kannan SA\\Desktop\\web_based_projects\\QueryResults (3).csv")
#print(dataset.head())
dataset['SQLite']=dataset['SQLite'].fillna(dataset['SQLite'].mode()[0])
dataset['Node.js']=dataset['Node.js'].fillna(dataset['Node.js'].mode()[0])
dataset['NoSQL']=dataset['NoSQL'].fillna(dataset['NoSQL'].mode()[0])
dataset['RDBMS']=dataset['RDBMS'].fillna(dataset['RDBMS'].mode()[0])
dataset['MongoDB']=dataset['MongoDB'].fillna(dataset['MongoDB'].mode()[0])
dataset['PostgerSQL']=dataset['PostgerSQL'].fillna(dataset['PostgerSQL'].mode()[0])
dataset['Swift']=dataset['Swift'].fillna(dataset['Swift'].mode()[0])
dataset['Scala']=dataset['Scala'].fillna(dataset['Scala'].mode()[0])
dataset['Windows']=dataset['Windows'].fillna(dataset['Windows'].mode()[0])
dataset['C/C++']=dataset['C/C++'].fillna(dataset['C/C++'].mode()[0])
dataset['Python']=dataset['Python'].fillna(dataset['Python'].mode()[0])
dataset['MATLAB']=dataset['MATLAB'].fillna(dataset['MATLAB'].mode()[0])
dataset.drop(['Unnamed: 52'],axis=1,inplace=True)
print(dataset.isnull().sum())
#print(dataset.columns)
#print(dataset.columns[8:-1])
x=dataset[dataset.columns[8:-1]]
y=dataset['Position']
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
nb=GaussianNB()
nb.fit(xtrain,ytrain)
#samp=np.array([1,1,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0])
ypred=nb.predict(xtest)     # ypred=rff.predict(samp.reshape(1,-1))
print("accuracy : ",accuracy_score(ytest,ypred))
#print(ypred)
#print(samp.reshape(1,-1))
#file='rfc_file.pkl'
#pickle.dump(rff,open(file,'wb'))
#print("done in creating pickel file")