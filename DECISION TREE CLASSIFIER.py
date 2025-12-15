import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# Dataset (replace with your own)
df = pd.DataFrame({
    'Outlook':['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast','Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temp':['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity':['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High'],
    'Wind':['Weak','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'Play':['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
})

# Encode
df = df.apply(lambda x: x.astype('category').cat.codes)

X = df.drop('Play', axis=1)
y = df['Play']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Decision Tree
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X_train, y_train)

# Display tree
print(export_text(model, feature_names=list(X.columns)))

# Predict & Accuracy
print("Prediction:", model.predict([[1,2,0,1]]))
print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))
