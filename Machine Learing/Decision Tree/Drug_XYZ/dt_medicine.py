import pandas as pd
drug = pd.read_csv('drug_XYZ_2.csv')

X = drug.drop(columns = ['Drug'])
y = drug['Drug']

model = DecisionTreeClassifier()
model.fit(X, y)
predictions = model.predict([ [22, 1, 2, 2, 25.355], [50, 0, 1, 2, 9.894]])
predictions



### predictions

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

drug = pd.read_csv('drug_XYZ_2.csv')
X = drug.drop(columns = ['Drug'])
y = drug['Drug']
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

score = accuracy_score(y_test, predictions)
