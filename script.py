import pandas as pd
import numpy as np
import requests
from datetime import datetime
import matplotlib.pyplot as plt

# Download Apple stock data
csv_url = "https://perplexity.ai/rest/finance/history/AAPL/csv?start_date=2017-08-29&end_date=2025-08-29"
response = requests.get(csv_url)
with open("apple_stock_data.csv", "wb") as f:
    f.write(response.content)

# Load the data
df = pd.read_csv("apple_stock_data.csv")
print("Apple Stock Data Shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn info:")
print(df.dtypes)
print("\nDate range:")
print("Start:", df['date'].min())
print("End:", df['date'].max())