import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score

df = pd.read_csv("data/archive/creditcard.csv") 
X = df.drop("Class", axis=1)
Y = df["Class"]
model = LogisticRegression()

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
) 
model.fit(X_train, Y_train)
predictions  = model.predict(X_test)

print(predictions[:10])
print(Y_test.iloc[:10].to_numpy())
# print(model.coef_)
# print(model.intercept_)

cm = confusion_matrix(Y_test, predictions)
print(cm)

precision = precision_score(Y_test, predictions)
recall = recall_score(Y_test, predictions)
print("Precision:", precision)
print("Recall:", recall)

probabilities = model.predict_proba(X_test)
print(probabilities[:5])

fraud_probabilities = probabilities[:,1]
print(fraud_probabilities[:5])

threshold = [0.5,0.4,0.3,0.2,0.1]
custom_predictions = (fraud_probabilities >= threshold).astype(int)
print(custom_predictions[:10])

custom_cm = confusion_matrix(Y_test, custom_predictions)
custom_precision = precision_score(Y_test, custom_predictions)
custom_recall = recall_score(Y_test, custom_predictions)

print(custom_cm)
print("Custom precision:", custom_precision)
print("Custom recall:", custom_recall)