import sys
import time
# Importing dataset from sklearn
import warnings

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

n_estimators = int(sys.argv[1])
warnings.filterwarnings(action='ignore', category=DeprecationWarning)


def main():
    df = pd.read_csv("dataset.csv")  # dataset loading

    df['target'] = df.index
    df.reset_index(drop=True)
    df.index = range(0, len(df))

    X = df.drop(['target'], axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # set xgboost params
    clf = XGBClassifier(n_estimators=n_estimators)

    temps1 = time.time()
    clf.fit(X_train, y_train)
    print(time.time() - temps1)
    # y_pred = clf.predict(X_test)
    # print(metrics.accuracy_score(y_test, y_pred))


if __name__ == '__main__':
    main()
