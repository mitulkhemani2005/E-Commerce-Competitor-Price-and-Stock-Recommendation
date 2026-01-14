from fastapi import FastAPI
import uvicorn
from data.create_db_schema import create_database_schema
from data.web_scrap_data import scrap_data
from process.data_cleaning import data_cleaning
from process.next_day_trend import next_day_review_price
from model.next_day_model_train import next_day_model_train
from model.next_day_predict import model_predict
from model.basemodel import productDetail

app = FastAPI()

@app.get('/')
def welcome():
    return ({'Message': 'FastAPI is Running Properly'})

@app.put('/create-db')
def create_db ():
    return create_database_schema()

@app.post('/product-data-fetch')
def product_data_fetch (product_url):
    return scrap_data(product_url)

@app.put('/clean-data')
def clean_data ():
    return data_cleaning()

@app.get('/next-day-trend')
def next_day_trend_analysis ():
    analyse_price, analyse_customer = next_day_review_price()
    return ({'Message':f"As per the last 7 days trend tomorrow's customer visit = {analyse_customer} and product price {analyse_price}"})

@app.get('/next-model-train')
def new_model_train ():
    return (next_day_model_train())

@app.post('/next-day-demand')
def predict_next_day (Product_input:productDetail):
    analyse_price, analyse_customer = (model_predict(**Product_input.dict()))
    return ({'Message':f"As per the last 7 days Model trend tomorrow's customer visit = {analyse_customer} and product price {analyse_price}"})
 