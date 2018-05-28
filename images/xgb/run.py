import sys
import time
# Importing dataset from sklearn
import warnings

from sklearn import datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

n_estimators = int(sys.argv[1])
warnings.filterwarnings(action='ignore', category=DeprecationWarning)


def main():
    iris = datasets.load_wine()  # dataset loading
    X = iris.data  # Features stored in X
    y = iris.target  # Class variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create an XGB classifier and instance of the same
    # set xgboost params
    clf = XGBClassifier(n_estimators=n_estimators)

    temps1 = time.time()
    clf.fit(X_train, y_train)
    print(time.time() - temps1)
    # y_pred = clf.predict(X_test)
    # print(metrics.accuracy_score(y_test, y_pred))


if __name__ == '__main__':
    main()
