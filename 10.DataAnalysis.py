import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
iris=pd.read_csv("iris.csv")
print("Shape of the Data set :",iris.shape)
print("First five rows")
print(iris.head())
print("***************")
print("Last five rows")
print(iris.tail())
print("Size of the Data Set :",iris.size)
print("Number of samples available for each Variety")
print(iris["variety"].value_counts())
print("Description of the data set")
print(iris.describe())
sns.pairplot(iris,hue="variety", kind="scatter",diag_kind="hist")
plt.style.use("dark_background")
sns.displot(iris.sepal_length,bins=10, color="g")
plt.title("Distribution of Sepal Length", fontsize=10, color="white")
plt.show()


  OUTPUT
=========


C:\Users\mlm\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\mlm\PycharmProjects\pythonProject\venv\dataset.py 
Shape of the Data set : (150, 5)
First five rows
   sepal_length  sepal_width  petal_length  petal_width variety
0           5.1          3.5           1.4          0.2  Setosa
1           4.9          3.0           1.4          0.2  Setosa
2           4.7          3.2           1.3          0.2  Setosa
3           4.6          3.1           1.5          0.2  Setosa
4           5.0          3.6           1.4          0.2  Setosa
***************
Last five rows
     sepal_length  sepal_width  petal_length  petal_width    variety
145           6.7          3.0           5.2          2.3  Virginica
146           6.3          2.5           5.0          1.9  Virginica
147           6.5          3.0           5.2          2.0  Virginica
148           6.2          3.4           5.4          2.3  Virginica
149           5.9          3.0           5.1          1.8  Virginica
Size of the Data Set : 750
Number of samples available for each Variety
variety
Versicolor    54
Virginica     50
Setosa        46
Name: count, dtype: int64
Description of the data set
       sepal_length  sepal_width  petal_length  petal_width
count    150.000000   150.000000    150.000000   150.000000
mean       5.843333     3.057333      3.758000     1.199333
std        0.828066     0.435866      1.765298     0.762238
min        4.300000     2.000000      1.000000     0.100000
25%        5.100000     2.800000      1.600000     0.300000
50%        5.800000     3.000000      4.350000     1.300000
75%        6.400000     3.300000      5.100000     1.800000
max        7.900000     4.400000      6.900000     2.500000

Process finished with exit code 0
