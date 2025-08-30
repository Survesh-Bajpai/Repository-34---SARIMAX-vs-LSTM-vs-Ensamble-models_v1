import plotly.graph_objects as go
import pandas as pd

# Data provided
dates = ["2017-08-29", "2018-01-01", "2018-06-01", "2019-01-01", "2019-06-01", "2020-01-01", "2020-06-01", "2021-01-01", "2021-06-01", "2022-01-01", "2022-06-01", "2023-01-01", "2023-06-01", "2024-01-01", "2024-06-01", "2025-08-28"]
prices = [40.73, 42.30, 46.28, 39.48, 53.26, 73.41, 91.20, 132.04, 140.15, 177.83, 147.96, 129.93, 189.25, 181.18, 214.10, 232.56]

# Convert dates to datetime
dates_dt = pd.to_datetime(dates)

# Create the figure
fig = go.Figure()

# Add the line trace
fig.add_trace(go.Scatter(
    x=dates_dt,
    y=prices,
    mode='lines',
    line=dict(color='#1FB8CD', width=3),
    name='Apple Stock',
    hovertemplate='Date: %{x}<br>Price: $%{y:.2f}<extra></extra>'
))

# Update layout
fig.update_layout(
    title="Apple Stock Price Performance (2017-2025)",
    xaxis_title="Date",
    yaxis_title="Price (USD)"
)

# Update traces
fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("apple_stock_chart.png")