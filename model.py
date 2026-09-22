import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score
from sklearn.preprocessing import StandardScaler 

df = pd.read_csv("data/archive/creditcard.csv") 
X = df.drop("Class", axis=1)
Y = df["Class"]
model = LogisticRegression(max_iter=1000)
scaler = StandardScaler()

X_train, X_temp, Y_train, Y_temp, = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
) 

X_validation, X_test, Y_validation, Y_test = train_test_split(
    X_temp,
    Y_temp,
    test_size= 0.5,
    random_state= 42,
    stratify= Y_temp
)

X_train_scaled = scaler.fit_transform(X_train)
X_validation_scaled = scaler.transform(X_validation)
X_test_scaled= scaler.transform(X_test)


model.fit(X_train_scaled, Y_train)
predictions  = model.predict(X_validation_scaled)

print(predictions[:10])
print(Y_validation.iloc[:10].to_numpy())
# print(model.coef_)
# print(model.intercept_)

cm = confusion_matrix(Y_validation, predictions)
print(cm)

precision = precision_score(Y_validation, predictions)
recall = recall_score(Y_validation, predictions)
print("Precision:", precision)
print("Recall:", recall)

probabilities = model.predict_proba(X_validation_scaled)
print(probabilities[:5])

fraud_probabilities = probabilities[:,1]
print(fraud_probabilities[:5])

thresholds = [0.9,0.5,0.4,0.3,0.2,0.1, 0.0000001]

for threshold in thresholds:
    custom_predictions = (fraud_probabilities >= threshold).astype(int)

    custom_cm = confusion_matrix(Y_validation, custom_predictions)
    custom_precision = precision_score(Y_validation, custom_predictions)
    custom_recall = recall_score(Y_validation, custom_predictions)

    print("Threshold:", threshold)
    print(custom_cm)
    print("Precision:", custom_precision)
    print("Recall:", custom_recall)



print(X_train.shape)
print(X_validation.shape)
print(X_test.shape)

print(Y_train.shape)
print(Y_validation.shape)
print(Y_test.shape)

print(Y_train.value_counts())
print(Y_validation.value_counts())
print(Y_test.value_counts())


new_custom_probabilities= model.predict_proba(X_test_scaled)
test_fraud_probabilities = new_custom_probabilities[:, 1]

threshold =0.1

custom_predictions = (test_fraud_probabilities >= threshold).astype(int)
custom_cm = confusion_matrix(Y_test, custom_predictions)
custom_precision = precision_score(Y_test, custom_predictions)
custom_recall = recall_score(Y_test, custom_predictions)

print("Final Test Results")
print("Threshold:", threshold)
print(custom_cm)
print("Precision:", custom_precision)
print("Recall:", custom_recall)
    
