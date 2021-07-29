from cleaning import *
from config import *
import preprocessor as pp
import pickle

data = clean_data(FILE_PATH_DATA)

X_train, X_test, y_train, y_test = pp.preprocess_data(dataframe=data)

# Logistic Regression Model
from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
logistic_prediction = logistic_model.predict(X_test)
test_score_log = round(logistic_model.score(X_test, y_test),2)

print(test_score_log)
# save the model to disk

pickle.dump(logistic_model, open(FILENAME_MODEL, 'wb'))