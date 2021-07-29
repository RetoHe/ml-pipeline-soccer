# Logistic Regression Model
from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
logistic_prediction = logistic_model.predict(X_test)
test_score_log = round(logistic_model.score(X_test, y_test),2)