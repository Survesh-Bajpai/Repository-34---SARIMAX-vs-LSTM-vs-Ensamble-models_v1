# Calculate fundamental indicators from financial data
print("Calculating fundamental indicators...")

# Process financial data
financials_df['date'] = pd.to_datetime(financials_df['date'])
balance_df['date'] = pd.to_datetime(balance_df['date'])

# Merge income statement with balance sheet
fundamentals = pd.merge(financials_df, balance_df, on=['date', 'calendarYear'], how='inner', suffixes=('_income', '_balance'))

# Calculate ROE (Return on Equity) = Net Income / Total Stockholders Equity
fundamentals['roe'] = fundamentals['netIncome'] / fundamentals['totalStockholdersEquity']

# Calculate ROCE (Return on Capital Employed) = Operating Income / (Total Assets - Current Liabilities)
# We'll use a simplified version: Operating Income / (Total Assets - Total Current Liabilities)
fundamentals['roce'] = fundamentals['operatingIncome'] / (fundamentals['totalAssets'] - fundamentals['totalCurrentLiabilities'])

# Calculate P/E ratio from financial data
current_price = 232.56  # Current Apple stock price
fundamentals['pe_ratio'] = current_price / fundamentals['epsdiluted']

# Calculate earnings growth rate for PEG ratio
fundamentals = fundamentals.sort_values('calendarYear').reset_index(drop=True)
fundamentals['earnings_growth'] = fundamentals['netIncome'].pct_change()

# Calculate PEG ratio = P/E ratio / (Earnings Growth Rate * 100)
# We'll use a reasonable growth rate for missing values
fundamentals['peg_ratio'] = fundamentals['pe_ratio'] / (fundamentals['earnings_growth'] * 100)

# Handle infinite and NaN values in PEG
fundamentals['peg_ratio'] = fundamentals['peg_ratio'].replace([np.inf, -np.inf], np.nan)

print(f"Fundamentals data shape: {fundamentals.shape}")
print("\nFundamental indicators calculated:")
print(fundamentals[['calendarYear', 'roe', 'roce', 'pe_ratio', 'peg_ratio']].head())

# Now we need to merge this with the stock data on a yearly basis
# We'll assign fundamentals to each day based on the fiscal year
df['year'] = df['date'].dt.year
df = df.merge(fundamentals[['calendarYear', 'roe', 'roce', 'peg_ratio']], 
              left_on='year', right_on='calendarYear', how='left')

print(f"\nFinal dataset shape: {df.shape}")
print("Columns in final dataset:")
print(df.columns.tolist())