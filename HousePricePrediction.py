from sklearn import linear_model #model importing
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error
from sklearn.model_selection import train_test_split
import pandas #to read data
import matplotlib.pyplot as plt #visualize the data features
import seaborn as sbn  #seaborn is to visualize the correlations from features using heatmap

df = pandas.read_csv("data.csv")

#print(df.head())

#To determine rows,col in dataframe
print("dataframe dimension", df.shape) 

#to print correlation matrix
print("correlation", df.corr())

#to draw heatmap for dataset
##plt.figure(figsize=(12,34))
##sbn.heatmap(df.corr(),annot=True,cmap='BrBG') 
#df.corr() - correlation it takes only numeric cols for finding correlation
#annot - to display values in cmap
#cmap -determines color for map

##plt.show()
#print(df.columns.values)


# X determines independent features

X = df.iloc[:,2:14]
y = df.iloc[:,1:2]
#y = df[["price"]]
print("y ", y)

#splitting the train and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8, test_size = 0.2, random_state=0)

model = linear_model.LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

#mean absolute percentage error
print("MEAN ERROR ", mean_absolute_percentage_error(y_pred,y_test))