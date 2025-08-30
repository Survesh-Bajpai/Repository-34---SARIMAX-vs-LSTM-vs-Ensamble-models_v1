# Download Apple financial data
financials_url = "https://perplexity.ai/rest/finance/financials/AAPL/csv?period=annual&statement_category=INCOME_STATEMENT"
response = requests.get(financials_url)
with open("apple_income_statement.csv", "wb") as f:
    f.write(response.content)

# Load the financial data
financials_df = pd.read_csv("apple_income_statement.csv")
print("Apple Income Statement Shape:", financials_df.shape)
print("\nFirst 2 rows:")
print(financials_df.head(2))
print("\nColumns:")
print(financials_df.columns.tolist())