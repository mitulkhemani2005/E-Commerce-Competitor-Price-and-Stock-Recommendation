import pandas as pd
import math
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import pickle

CLEANED_DATA = './data/predict.csv'
MODEL_PATH = './model/customer.pkl'

def next_day_review_price ():
    df = pd.read_csv(CLEANED_DATA)
    next_day_customer = math.floor((df['daily_review'].iloc[-7:].mean()))
    today_price = df.iloc[-1]['selling_price']
    price = [today_price * 0.95, today_price, today_price * 1.05]
    customers = [next_day_customer + 1, next_day_customer, max(next_day_customer - 1, 0)]
    revenue = [i*j for i,j in zip(price,customers)]
    max_revenue_index = 0
    for i in range(len(revenue)):
        if (revenue[max_revenue_index] < revenue[i]):
            max_revenue_index = i
    max_price = price[max_revenue_index]
    return max_price, next_day_customer