# Download Apple balance sheet data
balance_sheet_url = "https://perplexity.ai/rest/finance/financials/AAPL/csv?period=annual&statement_category=BALANCE_SHEET"
response = requests.get(balance_sheet_url)
with open("apple_balance_sheet.csv", "wb") as f:
    f.write(response.content)

# Load the balance sheet data
balance_df = pd.read_csv("apple_balance_sheet.csv")
print("Apple Balance Sheet Shape:", balance_df.shape)
print("\nFirst row:")
print(balance_df.head(1))
print("\nKey columns for ROE and ROCE:")
relevant_cols = ['date', 'calendarYear', 'totalStockholdersEquity', 'totalAssets', 'totalLiabilities']
print(balance_df[relevant_cols].head())