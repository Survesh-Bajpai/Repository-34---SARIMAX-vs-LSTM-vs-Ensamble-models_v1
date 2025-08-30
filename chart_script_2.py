import plotly.graph_objects as go
import pandas as pd

# Data from the provided JSON
data = {
    "comparisons": ["LSTM vs SARIMAX", "Ensemble vs LSTM", "Ensemble vs SARIMAX"],
    "effect_sizes": [0.505, 0.42, 0.785],
    "ci_lower": [0.12, 0.08, 0.34],
    "ci_upper": [0.89, 0.76, 1.23],
    "p_values": [0.023, 0.041, 0.001]
}

df = pd.DataFrame(data)

# Abbreviate comparison names to meet 15 character limit
abbreviated_comparisons = ["LSTM vs SARIMAX", "Ens vs LSTM", "Ens vs SARIMAX"]

# Determine colors based on significance levels
colors = []
for p in df['p_values']:
    if p < 0.001:
        colors.append('#1FB8CD')  # Strong cyan for highly significant (p < 0.001)
    elif p < 0.05:
        colors.append('#DB4545')  # Bright red for significant (p < 0.05)
    else:
        colors.append('#2E8B57')  # Sea green for not significant

# Calculate error bars for confidence intervals
error_x_minus = df['effect_sizes'] - df['ci_lower']
error_x_plus = df['ci_upper'] - df['effect_sizes']

# Create the horizontal bar chart
fig = go.Figure()

fig.add_trace(go.Bar(
    y=abbreviated_comparisons,
    x=df['effect_sizes'],
    orientation='h',
    marker_color=colors,
    error_x=dict(
        type='data',
        array=error_x_plus,
        arrayminus=error_x_minus,
        visible=True,
        thickness=3,
        width=8
    ),
    hovertemplate='<b>%{y}</b><br>Effect Size: %{x:.3f}<br>CI: [%{customdata[0]:.3f}, %{customdata[1]:.3f}]<br>p-value: %{customdata[2]:.3f}<extra></extra>',
    customdata=list(zip(df['ci_lower'], df['ci_upper'], df['p_values']))
))

# Add p-value annotations
for i, (comparison, p_val, effect_size) in enumerate(zip(abbreviated_comparisons, df['p_values'], df['effect_sizes'])):
    fig.add_annotation(
        x=effect_size + 0.1,
        y=i,
        text=f"p={p_val:.3f}",
        showarrow=False,
        font=dict(size=12),
        xanchor="left"
    )

fig.update_layout(
    title="Statistical Significance Testing Results (95% CI)",
    xaxis_title="Effect Size",
    yaxis_title="Model Compare"
)

fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("hypothesis_testing_chart.png")