from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X = data.drop(columns=["failure", "timestamp"])
y = data["failure"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

data["failure_prob"] = model.predict_proba(X)[:,1]