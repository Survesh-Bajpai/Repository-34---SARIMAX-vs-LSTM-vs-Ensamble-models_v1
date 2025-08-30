import plotly.graph_objects as go
import plotly.io as pio

# Data from the provided JSON
models = ["SARIMAX", "LSTM", "Ensemble"]
mae = [2.34, 1.89, 1.67]
rmse = [3.45, 2.76, 2.45]
mape = [1.87, 1.45, 1.32]
accuracy = [94.2, 95.8, 96.5]

# Brand colors in order
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F']

# Create the figure
fig = go.Figure()

# Add bars for each metric with proper grouping
fig.add_trace(go.Bar(
    name='MAE',
    x=models,
    y=mae,
    marker_color=colors[0]
))

fig.add_trace(go.Bar(
    name='RMSE',
    x=models,
    y=rmse,
    marker_color=colors[1]
))

fig.add_trace(go.Bar(
    name='MAPE',
    x=models,
    y=mape,
    marker_color=colors[2]
))

fig.add_trace(go.Bar(
    name='Accuracy (%)',
    x=models,
    y=accuracy,
    marker_color=colors[3]
))

# Update traces to prevent clipping
fig.update_traces(cliponaxis=False)

# Update layout with proper grouping and legend
fig.update_layout(
    title='Model Perf: SARIMAX vs LSTM vs Ensemble',
    xaxis_title='Models',
    yaxis_title='Perf Values',
    barmode='group',
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Save the chart
fig.write_image('model_performance_comparison.png')