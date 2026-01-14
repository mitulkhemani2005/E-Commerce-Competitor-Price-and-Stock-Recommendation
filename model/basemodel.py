from pydantic import BaseModel

class productDetail (BaseModel):
    original_price: float
    selling_price: float
    discount: float
    overall_rating: float	
    stock: str
    seller_rating: float	
    lag_1_review: float	
    lag_2_review: float
    rolling_3_review: float