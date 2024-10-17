import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
# Load the dataset
advertising = pd.read_csv('company_data.csv')
# Display the first few rows of the data
print(advertising.head())
#Scatter plot representation of data using seaborn
import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(advertising, x_vars=['TV', 'Radio', 'Newspaper'],
y_vars='Sales', height=5, aspect=1, kind='scatter')
plt.show()
# Assuming 'Sales' is the dependent variable and the rest are features
X = advertising.drop(columns=['Sales'])
y = advertising['Sales']
# Split the dataset into training and testing sets (80% training, 20% testing);
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Create the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
# Predict on the test data
y_pred = model.predict(X_test)
# Model evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
# Display results
print("\nMean Squared Error:", mse)
print("R-squared:", r2)
# Display the coefficients and intercept
print("\nCoefficients:", model.coef_)
print("Intercept:", model.intercept_)
#To Display Real Values and Predicted Values
y_pred = model.predict(X_test)
for(i,j) in zip(y_test,y_pred):
    if i!=j:
        print("Actual value :",i,"Predicted value :",j)
    print("\nNumber of mislabeled points from test data set :", (y_test != y_pred).sum())


 OUTPUT
========

C:\Users\MLM\PycharmProjects\pythonProject\DEVAN\Scripts\python.exe C:\Users\MLM\PycharmProjects\pythonProject\DEVAN\linear-regression.py 
      TV  Radio  Newspaper  Sales
0  230.1   37.8       69.2   22.1
1   44.5   39.3       45.1   10.4
2   17.2   45.9       69.3   12.0
3  151.5   41.3       58.5   16.5
4  180.8   10.8       58.4   17.9

Mean Squared Error: 3.6361007254487823
R-squared: 0.851010619688148

Coefficients: [ 0.05429703  0.11137464 -0.00145809]
Intercept: 4.687332657183493
Actual value : 14.8 Predicted value : 15.324359465893444

Number of mislabeled points from test data set : 40
Actual value : 19.0 Predicted value : 19.366510132047015

Number of mislabeled points from test data set : 40
Actual value : 13.6 Predicted value : 13.305513016087096

Number of mislabeled points from test data set : 40
Actual value : 11.6 Predicted value : 12.121811370101426

Number of mislabeled points from test data set : 40
Actual value : 16.4 Predicted value : 16.024688071879808

Number of mislabeled points from test data set : 40
Actual value : 25.4 Predicted value : 24.050128914574593

Number of mislabeled points from test data set : 40
Actual value : 15.9 Predicted value : 15.506712899149218

Number of mislabeled points from test data set : 40
Actual value : 8.7 Predicted value : 8.33035596012451

Number of mislabeled points from test data set : 40
Actual value : 10.4 Predicted value : 11.414814003288809

Number of mislabeled points from test data set : 40
Actual value : 20.7 Predicted value : 21.433307631159316

Number of mislabeled points from test data set : 40
Actual value : 20.7 Predicted value : 19.367113166518248

Number of mislabeled points from test data set : 40
Actual value : 1.6 Predicted value : 9.123090919940395

Number of mislabeled points from test data set : 40
Actual value : 16.0 Predicted value : 18.355017218614

Number of mislabeled points from test data set : 40
Actual value : 20.2 Predicted value : 17.131015855154473

Number of mislabeled points from test data set : 40
Actual value : 17.1 Predicted value : 18.92736858996132

Number of mislabeled points from test data set : 40
Actual value : 5.6 Predicted value : 7.102588974109013

Number of mislabeled points from test data set : 40
Actual value : 14.6 Predicted value : 15.319289648888395

Number of mislabeled points from test data set : 40
Actual value : 16.1 Predicted value : 21.422667343553467

Number of mislabeled points from test data set : 40
Actual value : 17.2 Predicted value : 16.605687352033545

Number of mislabeled points from test data set : 40
Actual value : 12.6 Predicted value : 12.586310710700499

Number of mislabeled points from test data set : 40
Actual value : 5.9 Predicted value : 6.031801968378788

Number of mislabeled points from test data set : 40
Actual value : 20.9 Predicted value : 21.758995997995264

Number of mislabeled points from test data set : 40
Actual value : 22.1 Predicted value : 21.290140979762104

Number of mislabeled points from test data set : 40
Actual value : 11.9 Predicted value : 9.980856043403225

Number of mislabeled points from test data set : 40
Actual value : 13.2 Predicted value : 13.379864840588493

Number of mislabeled points from test data set : 40
Actual value : 13.2 Predicted value : 14.196777027053711

Number of mislabeled points from test data set : 40
Actual value : 14.7 Predicted value : 14.178593335601636

Number of mislabeled points from test data set : 40
Actual value : 18.4 Predicted value : 19.399708657687903

Number of mislabeled points from test data set : 40
Actual value : 11.0 Predicted value : 11.809691068784293

Number of mislabeled points from test data set : 40
Actual value : 12.0 Predicted value : 11.869669248666511

Number of mislabeled points from test data set : 40
Actual value : 24.4 Predicted value : 24.29559141035417

Number of mislabeled points from test data set : 40
Actual value : 17.6 Predicted value : 20.796456178230557

Number of mislabeled points from test data set : 40
Actual value : 9.6 Predicted value : 9.876817298416999

Number of mislabeled points from test data set : 40
Actual value : 16.7 Predicted value : 14.746084710456161

Number of mislabeled points from test data set : 40
Actual value : 15.0 Predicted value : 17.256649163561022

Number of mislabeled points from test data set : 40
Actual value : 14.6 Predicted value : 14.095389486694499

Number of mislabeled points from test data set : 40
Actual value : 21.5 Predicted value : 21.21922069333582

Number of mislabeled points from test data set : 40
Actual value : 17.5 Predicted value : 18.1111932991006

Number of mislabeled points from test data set : 40
Actual value : 16.9 Predicted value : 17.675014115782524

Number of mislabeled points from test data set : 40
Actual value : 15.5 Predicted value : 13.467719584179173

Number of mislabeled points from test data set : 40

Process finished with exit code 0
