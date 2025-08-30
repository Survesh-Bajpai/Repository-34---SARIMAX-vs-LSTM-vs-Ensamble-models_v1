# Fix the date issue and merge properly
print("Processing dates and merging data...")

# Ensure dates are properly parsed
df['date'] = pd.to_datetime(df['date'], utc=True)
df['year'] = df['date'].dt.year

print(f"Stock data years range: {df['year'].min()} to {df['year'].max()}")
print(f"Fundamentals years available: {sorted(fundamentals['calendarYear'].unique())}")

# Merge fundamentals with stock data
df = df.merge(fundamentals[['calendarYear', 'roe', 'roce', 'peg_ratio']], 
              left_on='year', right_on='calendarYear', how='left')

# Clean up the dataset by removing rows with too many NaN values (first 50 rows typically have NaN for technical indicators)
df_clean = df.dropna(subset=['volatility', 'rsi', 'macd'])

print(f"Final clean dataset shape: {df_clean.shape}")
print(f"Date range: {df_clean['date'].min()} to {df_clean['date'].max()}")

# Display summary of all features
feature_cols = ['volume', 'volatility', 'roe', 'roce', 'peg_ratio', 'macd', 'ema_12', 'ema_26', 'ema_50', 'parabolic_sar', 'rsi']
print(f"\nFeatures summary:")
print(df_clean[feature_cols].describe())

# Save the processed dataset
df_clean.to_csv("apple_processed_data.csv", index=False)
print("\nProcessed data saved to 'apple_processed_data.csv'")

# Show recent data
print("\nRecent data sample:")
print(df_clean[['date', 'close'] + feature_cols].tail())