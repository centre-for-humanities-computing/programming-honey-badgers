import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report

def assign01(data):
    print("[INFO] solution to assigment 1")
    idxs0 = data['sign'] == 'virgo'
    idxs1 = data['sign'] == 'pisces'
    idxs = idxs0.values + idxs1.values
    corpus = data['horoscope'].loc[idxs]
    cv = CountVectorizer()
    X = cv.fit_transform(corpus.values).toarray()
    y = data['sign'].loc[idxs].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)
    classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
    print(f'Correctly classified instances {accuracy_score(y_test, y_pred, normalize=False)}')

    print(classification_report(y_test, y_pred))#target_names=target_names))

    return (accuracy_score(y_test, y_pred), cm)



def assign02(data):
    print("[INFO] solution to assigment 2")
    idxs0 = data['sign'] == 'virgo'
    idxs1 = data['sign'] == 'pisces'
    idxs = idxs0.values + idxs1.values
    corpus = data['horoscope'].loc[idxs]
    cv = CountVectorizer(max_df=.75, min_df=10, stop_words='english', max_features=1000, ngram_range=(1, 3))
    X = cv.fit_transform(corpus.values).toarray()
    print(X.shape)
    y = data['sign'].loc[idxs].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)
    classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
    print(f'Correctly classified instances {accuracy_score(y_test, y_pred, normalize=False)}')
    print(classification_report(y_test, y_pred))
    return (accuracy_score(y_test, y_pred), cm)


def assign03(data):
    print("[INFO] solution to assigment 3")
    corpus = data['horoscope']
    cv = CountVectorizer()
    X = cv.fit_transform(corpus.values).toarray()
    y = data['sign'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20)
    classifier = MultinomialNB(alpha=1.0, class_prior=None, fit_prior=True)
    classifier.fit(X_train , y_train)
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(f'Relative Accuracy; {accuracy_score(y_test, y_pred)}')
    print(f'Correctly classified instances {accuracy_score(y_test, y_pred, normalize=False)}')
    print(classification_report(y_test, y_pred))
    return (accuracy_score(y_test, y_pred), cm)


def main():
    data = pd.read_csv('dat/horoscopes.csv')
    data.drop_duplicates(inplace=True)
    print(data.columns)

    assign01(data)
    assign02(data)

    print(f'[INFO] zero rate performance {data["sign"].value_counts().max()/data.shape[0]}')
    assign03(data)

    
if __name__ == '__main__':
    main()