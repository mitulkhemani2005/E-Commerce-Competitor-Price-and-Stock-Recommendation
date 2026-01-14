import pickle
import pandas
import numpy as np
import math

MODEL_PATH = './model/customer.pkl'
ENCODER_PATH = './model/encoder.pkl'
SCALER_PATH = './model/scaler.pkl'

def model_predict(original_price,selling_price,discount,overall_rating,stock,seller_rating,lag_1_review,lag_2_review,rolling_3_review):
    with open (MODEL_PATH , 'rb') as f:
        model = pickle.load(f)
    with open (ENCODER_PATH , 'rb') as f:
        encoder = pickle.load(f)
    with open (SCALER_PATH , 'rb') as f:
        scaler = pickle.load(f)
    
    stock_encode = encoder.transform([stock])[0]
    model_input = np.array([[original_price,selling_price,discount,overall_rating,stock_encode,seller_rating,lag_1_review,lag_2_review,rolling_3_review]])
    model_input_scaler = scaler.transform(model_input)
    next_day_customer = math.floor(model.predict(model_input_scaler)[0])
    today_price = selling_price
    price = [today_price * 0.95, today_price, today_price * 1.05]
    customers = [next_day_customer + 1, next_day_customer, max(next_day_customer - 1, 0)]
    revenue = [i*j for i,j in zip(price,customers)]
    max_revenue_index = 0
    for i in range(len(revenue)):
        if (revenue[max_revenue_index] < revenue[i]):
            max_revenue_index = i
    max_price = price[max_revenue_index]
    return max_price, next_day_customer