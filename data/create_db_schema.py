import sqlite3
SALES_DATA = './data/sales.db'

def create_database_schema():
    try:
        conn = sqlite3.connect(SALES_DATA, check_same_thread=False)
        curr = conn.cursor()
        curr.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                date varchar(20),
                time varchar(20),
                name varchar(100),
                original_price float,
                selling_price float,
                discount float,
                overall_rating float,
                ratings int,
                reviews int,
                stock varchar(20),
                seller_name varchar(50),
                seller_rating float,
                url varchar(1000)
            );
        """)
        conn.commit()
        conn.close()
        return ({'Message':'Database Schema Created Successful'})
    except Exception as ex:
        return ({'Message':f'Database Schema Failed Error: {ex}'})
    