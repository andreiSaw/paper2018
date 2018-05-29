import sys
import time
import warnings

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

nthread = int(sys.argv[1])
warnings.filterwarnings(action='ignore', category=DeprecationWarning)


def main():
    df = pd.read_csv("/input/images/xgb/nursery.data.txt", header=None)  # dataset loading
    df.columns = ['parents', 'has_nurs', 'form', 'children', 'housing', 'finance', 'social', 'health', 'target']
    from sklearn import preprocessing
    def transform(feature):
        le = preprocessing.LabelEncoder()
        le.fit(df[feature])
        df[feature] = le.transform(df[feature])

    for feature in df.columns:
        transform(feature)

    X = df.drop(['target'], axis=1)
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # print(len(X_train))

    # set xgboost params
    clf = XGBClassifier(nthread=nthread)

    temps1 = time.time()
    clf.fit(X_train, y_train)
    print(time.time() - temps1)


if __name__ == '__main__':
    main()
