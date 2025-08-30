# Calculate technical indicators manually
import pandas as pd
import numpy as np

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date').reset_index(drop=True)

print("Calculating technical indicators manually...")

# 1. Volatility (20-day rolling standard deviation of returns)
df['returns'] = df['close'].pct_change()
df['volatility'] = df['returns'].rolling(window=20).std() * np.sqrt(252)  # Annualized volatility

# 2. RSI (Relative Strength Index) - 14-day period
def calculate_rsi(prices, window=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

df['rsi'] = calculate_rsi(df['close'])

# 3. EMA (Exponential Moving Average)
def calculate_ema(prices, window):
    return prices.ewm(span=window).mean()

df['ema_12'] = calculate_ema(df['close'], 12)
df['ema_26'] = calculate_ema(df['close'], 26)
df['ema_50'] = calculate_ema(df['close'], 50)

# 4. MACD (Moving Average Convergence Divergence)
df['macd'] = df['ema_12'] - df['ema_26']
df['macd_signal'] = calculate_ema(df['macd'], 9)
df['macd_hist'] = df['macd'] - df['macd_signal']

# 5. Parabolic SAR (simplified version)
def calculate_parabolic_sar(high, low, af_start=0.02, af_increment=0.02, af_max=0.2):
    length = len(high)
    psar = np.zeros(length)
    af = af_start
    ep = high[0]
    trend = 1  # 1 for uptrend, -1 for downtrend
    
    psar[0] = low[0]
    
    for i in range(1, length):
        if trend == 1:  # Uptrend
            psar[i] = psar[i-1] + af * (ep - psar[i-1])
            if high[i] > ep:
                ep = high[i]
                af = min(af + af_increment, af_max)
            if low[i] <= psar[i]:
                trend = -1
                psar[i] = ep
                af = af_start
                ep = low[i]
        else:  # Downtrend
            psar[i] = psar[i-1] + af * (ep - psar[i-1])
            if low[i] < ep:
                ep = low[i]
                af = min(af + af_increment, af_max)
            if high[i] >= psar[i]:
                trend = 1
                psar[i] = ep
                af = af_start
                ep = high[i]
    
    return psar

df['parabolic_sar'] = calculate_parabolic_sar(df['high'].values, df['low'].values)

print("Technical indicators calculated successfully!")
print(f"Data shape after technical indicators: {df.shape}")
print("\nFirst few rows with indicators:")
print(df[['date', 'close', 'volatility', 'macd', 'ema_12', 'rsi']].head())