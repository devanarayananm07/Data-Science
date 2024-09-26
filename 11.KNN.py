import numpy as np
import pandas as pd
dataset = pd.read_csv("iris.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
from sklearn.metrics import accuracy_score
print ("Accuracy : ", accuracy_score(y_test, y_pred))
df = pd.DataFrame({'Real Values':y_test, 'Predicted Values':y_pred})
print(df)
new_test_point = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = classifier.predict(new_test_point)
print(f"\n Predicted class: {prediction[0]}")



OUTPUT
-------

C:\Users\mlm\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\mlm\PycharmProjects\pythonProject\venv\knn.py 
              precision    recall  f1-score   support

      Setosa       0.80      1.00      0.89         8
  Versicolor       1.00      0.83      0.91        12
   Virginica       1.00      1.00      1.00        10

    accuracy                           0.93        30
   macro avg       0.93      0.94      0.93        30
weighted avg       0.95      0.93      0.93        30

Accuracy :  0.9333333333333333
   Real Values Predicted Values
0    Virginica        Virginica
1       Setosa           Setosa
2   Versicolor       Versicolor
3    Virginica        Virginica
4   Versicolor       Versicolor
5       Setosa           Setosa
6       Setosa           Setosa
7       Setosa           Setosa
8   Versicolor       Versicolor
9   Versicolor       Versicolor
10  Versicolor       Versicolor
11  Versicolor       Versicolor
12      Setosa           Setosa
13   Virginica        Virginica
14   Virginica        Virginica
15   Virginica        Virginica
16   Virginica        Virginica
17   Virginica        Virginica
18  Versicolor           Setosa
19  Versicolor           Setosa
20  Versicolor       Versicolor
21   Virginica        Virginica
22  Versicolor       Versicolor
23   Virginica        Virginica
24   Virginica        Virginica
25      Setosa           Setosa
26      Setosa           Setosa
27      Setosa           Setosa
28  Versicolor       Versicolor
29  Versicolor       Versicolor

 Predicted class: Setosa

Process finished with exit code 0
