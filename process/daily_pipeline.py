from data.web_scrap_data import scrap_data
from process.data_cleaning import data_cleaning
from model.next_day_model_train import next_day_model_train
url = 'https://www.flipkart.com/apple-macbook-air-m4-16-gb-256-gb-ssd-macos-sequoia-mc6t4hn-a/p/itm7c1831ce25509?pid=COMH9ZWQCJGMZGXE&lid=LSTCOMH9ZWQCJGMZGXEBSSIQU&marketplace=FLIPKART&q=mac+book&store=6bo%2Fb5g&srno=s_1_3&otracker=search&otracker1=search&fm=organic&iid=06fe88d4-be33-45d4-8fc3-ac416df21ab6.COMH9ZWQCJGMZGXE.SEARCH&ppt=None&ppn=None&ssid=sdo0b0r1ts0000001768385812403&qH=e1dadd2eac76bb48'

def run_daily_pipeline():
    print('Daily Pipeline Started')
    scrap_data(url)
    data_cleaning()
    next_day_model_train()
    print('Daily Pipeline Completed')

if __name__ == '__main__':
    run_daily_pipeline()