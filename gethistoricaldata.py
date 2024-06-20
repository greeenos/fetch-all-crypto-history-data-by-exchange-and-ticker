import ccxt
import csv
import time
from datetime import datetime, timedelta
from tqdm import tqdm
import os
import pandas as pd

###########################
# INPUTS
symbol = 'BTC/USDT' #what symbol to fetch
timeframe = '1m' #which timeframe to fetch ()

# Define start date
start_date = '2019-09-09'
###########################

# Initialize exchange
exchange = ccxt.binance({
    'options': {
        'defaultType': 'future',
    },
})

# Extract the first name of the exchange
exchange_name = exchange.name.split()[0]

limit = 2000

# Define function to convert date to milliseconds
def date_to_milliseconds(date_str):
    epoch = datetime.fromtimestamp(0)
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return int((dt - epoch).total_seconds() * 1000.0)

# Define function to convert milliseconds to date
def milliseconds_to_date(milliseconds):
    return datetime.fromtimestamp(milliseconds / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

# Define function to fetch OHLCV data by day
def fetch_all_ohlcv_by_day(symbol, timeframe, start_date, end_date):
    all_ohlcv = []
    current_date = start_date
    days_range = (datetime.strptime(end_date, "%Y-%m-%d") - datetime.strptime(start_date, "%Y-%m-%d")).days

    with tqdm(total=days_range, desc="Fetching data by day") as pbar:
        while current_date <= end_date:
            since = date_to_milliseconds(current_date)
            until = since + 24 * 60 * 60 * 1000
            while True:
                try:
                    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, since=since, limit=limit)
                    if len(ohlcv) == 0:
                        break
                    all_ohlcv.extend(ohlcv)
                    since = ohlcv[-1][0] + 1
                    time.sleep(exchange.rateLimit / 1000)
                    if since >= until:
                        break
                except Exception as e:
                    print(f"An error occurred: {e}")
                    break
            current_date = (datetime.strptime(current_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")
            pbar.update(1)
    
    return all_ohlcv

# Define function to fetch OHLCV data by month
def fetch_all_ohlcv_by_month(symbol, timeframe, start_date):
    current_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.now()
    months_range = (end_date.year - current_date.year) * 12 + end_date.month - current_date.month

    month_files = []
    output_dir = 'Monts'
    os.makedirs(output_dir, exist_ok=True)

    with tqdm(total=months_range, desc="Fetching data by month") as pbar:
        while current_date <= end_date:
            month_start = current_date.strftime("%Y-%m-%d")
            month_end = (current_date + timedelta(days=32)).replace(day=1) - timedelta(days=1)
            month_end = month_end.strftime("%Y-%m-%d")
            
            print(f"Fetching data for {month_start} to {month_end}")
            ohlcv_data = fetch_all_ohlcv_by_day(symbol, timeframe, month_start, month_end)
            
            if ohlcv_data:
                filename = os.path.join(output_dir, f'{exchange_name}_ohlcv_{month_start[:7]}.csv')
                with open(filename, mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['timestamp', 'open', 'high', 'low', 'close', 'volume'])
                    for row in ohlcv_data:
                        row[0] = milliseconds_to_date(row[0])
                        writer.writerow(row)
                print(f"Data for {month_start[:7]} have been saved to {filename}")
                month_files.append(filename)

            current_date = (current_date + timedelta(days=32)).replace(day=1)
            pbar.update(1)

    combined_filename = 'final_OHLC.csv'
    combined_data = pd.concat([pd.read_csv(file) for file in month_files])
    combined_data.drop_duplicates(subset=['timestamp'], keep='first', inplace=True)
    combined_data.sort_values(by='timestamp', inplace=True)
    combined_data.to_csv(combined_filename, index=False)

    print(f"All data have been combined and saved to {combined_filename}")

# Fetch all data and save by month to CSV files
fetch_all_ohlcv_by_month(symbol, timeframe, start_date)
