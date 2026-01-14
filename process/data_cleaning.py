import sqlite3
import pandas as pd

DATABASE_PATH = './data/sales.db'
CLEANED_PATH = './data/predict.csv'

def data_cleaning ():
    conn = sqlite3.connect(DATABASE_PATH)
    df = pd.read_sql("SELECT * FROM sales", conn)
    df['total_rating'] = df['ratings']+df['reviews']
    df['daily_review'] = df['total_rating'].diff()
    df.drop(['name','seller_name','url','ratings','reviews','total_rating', 'date', 'time'], axis=1, inplace=True)
    df["lag_1_review"] = df["daily_review"].shift(1)
    df["lag_2_review"] = df["daily_review"].shift(2)
    df["rolling_3_review"] = df["daily_review"].rolling(3).mean()
    df = df.fillna(0)
    df.to_csv(CLEANED_PATH, index=False)
    return ({'Message':'Data Cleaning Successful'}) 