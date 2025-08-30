# Process stock data and calculate technical indicators
import talib

# Convert date to datetime
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date').reset_index(drop=True)

# Basic price data
high = df['high'].values
low = df['low'].values  
close = df['close'].values
volume = df['volume'].values
open_prices = df['open'].values

print("Calculating technical indicators...")

# 1. Volatility (20-day rolling standard deviation of returns)
returns = df['close'].pct_change()
df['volatility'] = returns.rolling(window=20).std() * np.sqrt(252)  # Annualized volatility

# 2. MACD (Moving Average Convergence Divergence)
macd, macd_signal, macd_hist = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
df['macd'] = macd
df['macd_signal'] = macd_signal
df['macd_hist'] = macd_hist

# 3. EMA (Exponential Moving Averages)
df['ema_12'] = talib.EMA(close, timeperiod=12)
df['ema_26'] = talib.EMA(close, timeperiod=26)
df['ema_50'] = talib.EMA(close, timeperiod=50)

# 4. Parabolic SAR
df['parabolic_sar'] = talib.SAR(high, low, acceleration=0.02, maximum=0.2)

# 5. RSI (Relative Strength Index)
df['rsi'] = talib.RSI(close, timeperiod=14)

# 6. Volume (already in the data)
df['volume'] = volume

print("Technical indicators calculated successfully!")
print(f"Data shape after technical indicators: {df.shape}")
print("\nFirst few rows with indicators:")
print(df[['date', 'close', 'volatility', 'macd', 'ema_12', 'rsi']].head())