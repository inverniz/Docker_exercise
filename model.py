import pandas as pd
from os import makedirs
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle

def load_dataset():
    reading_filepath = 'data/juniorMLE_dataset.csv'
    dataset = pd.read_csv(reading_filepath,
                      usecols = ['IsQuestionForCommunity', 'VisitsLastYear', 'QuestionTextLength'],
                      dtype = {'IsQuestionForCommunity': int, 'VisitsLastYear': int, 'QuestionTextLength': int})

    X = dataset[['VisitsLastYear', 'QuestionTextLength']]
    y = dataset['IsQuestionForCommunity']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    return X_train, X_test, y_train, y_test

def train_classifier(X, y):
    logistic_classifier = LogisticRegression()
    logistic_classifier.fit(X, y)
    return logistic_classifier

def eval_classifier(classifier, X, y):
    predictions = classifier.predict(X)
    accuracy = accuracy_score(y, predictions)
    return accuracy

def save_classifier(classifier):
    makedirs('models', exist_ok=True)
    writing_filepath = 'models/logistic_regression.pkl'
    pickle.dump(classifier, open(writing_filepath, 'wb'))

if __name__ == '__main__':
    X_train, X_test, y_train, y_test = load_dataset()
    trained_classifier = train_classifier(X_train, y_train)
    accuracy_score = eval_classifier(trained_classifier, X_test, y_test)
    print("accuracy score: {}".format(accuracy_score))
    save_classifier(trained_classifier)


