import pickle

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error, root_mean_squared_error


# parameters

n_splits = 5
output_file = f'model_1.bin'

# data preparation

df = pd.read_csv("./data/StudentPerformanceFactors.csv")

df["Extracurricular_Activities"] = (df["Extracurricular_Activities"] == "Yes").astype(int)
df["Internet_Access"] = (df["Internet_Access"] == "Yes").astype(int)
df["Learning_Disabilities"] = (df["Learning_Disabilities"] == "Yes").astype(int)

df["School_Public"] = (df["School_Type"] == "Public").astype(int)
df["Gender_Male"] = (df["Gender"] == "Male").astype(int)

del df["School_Type"], df["Gender"]

df = df.dropna().reset_index(drop=True)

selected_features = ['Hours_Studied', 'Attendance', 'Parental_Involvement',
       'Access_to_Resources', 'Extracurricular_Activities', 'Sleep_Hours',
       'Previous_Scores', 'Motivation_Level', 'Internet_Access',
       'Tutoring_Sessions', 'Family_Income', 'Teacher_Quality',
       'Peer_Influence', 'Physical_Activity', 'Learning_Disabilities',
       'Parental_Education_Level', 'Distance_from_Home']

df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=42)


# training 

def train(df_final_train, y_train):
    """
    trains the model and the dict vectorizer.
    
    Args:
        df_final_train (pandas DataFrame): feature matrix to train the model 
        y_train (pandas Series): Label (Exam Scores)
        C (float): regularization parameter for Linear Regression model
        max_iterations (int): max iterations hyper parameter for Linear Regression model
    
    Returns
        dv: dict vectorizer to one hot encode numerical values
        model: trained Linear Regression model
    """
    dict_train = df_final_train[selected_features].to_dict(orient='records')

    dv = DictVectorizer(sparse=False)

    X_train = dv.fit_transform(dict_train)

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return dv, model


def predict(df_predict, dv, model):
    """
    predicts the exam scores of given examples
    
    Args:
        df_predict (pandas DataFrame): feature matrix to predict exam score 
        dv: dict vectorizer to one hot encode numerical values
        model (sklearn.linear_model.LinearRegression): trained Linear Regression model

    Returns
        y_pred (Pandas Series): predicted labels for the given examples
    """
    dict_predict = df_predict[selected_features].to_dict(orient='records')

    X_predict = dv.transform(dict_predict)
    y_pred = model.predict(X_predict)

    return y_pred


# validation

print(f'doing validation with model_1')

kfold = KFold(n_splits=n_splits, shuffle=True, random_state=42)

scores = []

fold = 0

for train_idx, val_idx in kfold.split(df_full_train):
    df_train = df_full_train.iloc[train_idx]
    df_val = df_full_train.iloc[val_idx]

    y_train = df_train.Exam_Score.values
    y_val = df_val.Exam_Score.values

    dv, model = train(df_train, y_train)
    y_pred = predict(df_val, dv, model)

    rmse = root_mean_squared_error(y_val, y_pred)
    scores.append(rmse)

    print(f'rmse on fold {fold} is {rmse}')
    fold = fold + 1


print('validation results:')
print('model_1: %.3f +- %.3f' % (np.mean(scores), np.std(scores)))


# training the final model

print('training the final model')

dv, model = train(df_full_train, df_full_train.Exam_Score.values)
y_pred = predict(df_test, dv, model)

y_test = df_test.Exam_Score.values
rmse = root_mean_squared_error(y_test, y_pred)

print(f'rmse={rmse}')


# Save the model

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'the model is saved to {output_file}')