import numpy as np
import pandas as pd
dataset = pd.read_csv('iris.csv')
X = dataset.iloc[:,:4].values
y = dataset['variety'].values
#split iris data to test and train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
#implement Gaussian
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
print("\n",y_pred,"\n")
# Find the accuracy level of the predicted value
from sklearn.metrics import accuracy_score
print ("\n Accuracy : ", accuracy_score(y_test, y_pred))
# Calculate the number of mislabeled instances
mislabeled_count = (y_test != y_pred).sum()
# Print the number of mislabeled instances
print(f"\n Number of mislabeled points: {mislabeled_count} out of{len(y_test)}")
# List out the class labels of the mismatching records
mismatches = (y_test != y_pred)
print("\n Mismatching records (Actual vs Predicted):")
for actual, predicted in zip(y_test[mismatches], y_pred[mismatches]):
    print(f"Actual: {actual}, Predicted: {predicted}")

  OUTPUT
 =======

C:\Users\MLM\PycharmProjects\pythonProject\DEVAN\Scripts\python.exe C:\Users\MLM\PycharmProjects\pythonProject\DEVAN\naive-bayes.py 

 ['Setosa' 'Virginica' 'Virginica' 'Setosa' 'Setosa' 'Virginica'
 'Versicolor' 'Setosa' 'Versicolor' 'Versicolor' 'Versicolor' 'Setosa'
 'Versicolor' 'Setosa' 'Setosa' 'Virginica' 'Setosa' 'Setosa' 'Setosa'
 'Virginica' 'Setosa' 'Versicolor' 'Virginica' 'Virginica' 'Versicolor'
 'Virginica' 'Setosa' 'Setosa' 'Versicolor' 'Versicolor'] 


 Accuracy :  0.8666666666666667

 Number of mislabeled points: 4 out of30

 Mismatching records (Actual vs Predicted):
Actual: Versicolor, Predicted: Setosa
Actual: Versicolor, Predicted: Setosa
Actual: Versicolor, Predicted: Virginica
Actual: Virginica, Predicted: Versicolor

Process finished with exit code 0
