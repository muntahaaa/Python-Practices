import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
# Load the Excel file
print("Loading the dataset...")
data = pd.read_excel('D://ML_idea/classDataset.xlsx')

# Check the first few rows
"""print("Displaying the first few rows of the dataset:")
print(data.head())"""
features = data[['Study hours','Marks in previous grade', 'class performance out of 10']]
#print(features.head())
label = data[['Marks scored']]
final_label= label * 100 
#print(final_label)

mdl= KNeighborsClassifier()
mdl.fit(features,final_label)
study_hours = int(input('How many hours your student study per day: '))
 
marks_previous = int(input('How much he scored in his previous grade give your answer in percentage: '))
 
mp = marks_previous / 100
 
class_performance = int(input('What is class performance of student out of 10: '))
 
prediction = mdl.predict([[study_hours, mp, class_performance]])
 
print('Predicted marks: ')
print(prediction)

