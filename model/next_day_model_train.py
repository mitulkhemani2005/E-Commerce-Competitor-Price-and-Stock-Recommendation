import pandas as pd
import math
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pickle
import os

MODEL_PATH = './model/customer.pkl'
ENCODER_PATH = './model/encoder.pkl'
SCALER_PATH = './model/scaler.pkl'
CLEANED_PATH = './data/predict.csv'

 
def next_day_model_train ():
    df = pd.read_csv(CLEANED_PATH)
    X = df.drop('daily_review', axis=1)
    y = df['daily_review']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    le = LabelEncoder()
    X_train['stock']= le.fit_transform(X_train['stock'])
    X_test['stock'] = le.transform(X_test['stock'])
    ss = StandardScaler()
    X_train_scale = ss.fit_transform(X_train)
    X_test_scale = ss.transform(X_test)
    if os.path.exists(MODEL_PATH):
        with open (MODEL_PATH, 'rb') as f:
            xgb = pickle.load(f)
        xgb.fit(X_train_scale, y_train, xgb_model=xgb.get_booster())  
    else:
        xgb = XGBRegressor()
        xgb.fit(X_train_scale, y_train)

    with open (MODEL_PATH, 'wb') as f:
        pickle.dump(xgb, f)
    with open (ENCODER_PATH, 'wb') as f:
        pickle.dump(le, f)
    with open (SCALER_PATH, 'wb') as f:
        pickle.dump(ss, f)
    return ({'Message':"New Model Trained Success"})