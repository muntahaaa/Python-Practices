import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

df= pd.read_csv('D://ML_idea/irisdata.csv')
#df.columns = ['sepal length', 'sepal width', 'petal length', 
     #         'petal width', 'species']
#print(df.head())
print(df.columns)

features = df[['petal length', 'petal width', 'sepal length', 'sepal width']]
label = df['species']
model = KNeighborsClassifier()
 
model.fit(features, label)
print('Flower species: ')
print(model.predict([[2, 3, 1, 2]]))

