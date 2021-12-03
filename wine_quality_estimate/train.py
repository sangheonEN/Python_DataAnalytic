import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


def accuracy(T, P):
    score = np.mean(T == P)
    return score


if __name__ == "__main__":

    # data load
    train = pd.read_csv("./dataset/train.csv")

    # type column: str convert int
    str_to_int = {"white":0, "red":1}
    train['type'] = train['type'].replace(str_to_int)

    print(train)

    # 독립변수(X), 종속변수(Y) 정의
    X = train.drop(['id', 'quality'], axis=1)
    Y = train['quality']

    # classifier trainer
    from sklearn.ensemble import RandomForestClassifier
    from lightgbm import LGBMClassifier
    from sklearn.model_selection import cross_validate
    from xgboost import XGBClassifier
    from sklearn.model_selection import GridSearchCV
    from sklearn.tree import DecisionTreeClassifier


    model = RandomForestClassifier(random_state=200, n_jobs=-1)

    model.fit(X, Y)

    scores = cross_validate(model, X, Y, return_train_score=True, n_jobs=-1)

    print(np.mean(scores['train_score']), np.mean(scores['test_score']))
    # print(model.feature_importances_)

    # test data
    test = pd.read_csv("./dataset/test.csv")
    test['type'] = test['type'].replace(str_to_int)

    submission = pd.read_csv("./dataset/sample_submission.csv")

    prediction = model.predict(test.drop('id', axis= 1))

    submission["quality"] = prediction

    submission.to_csv("./result/submission.csv", index=False)









