import plotly.graph_objects as go
import plotly.express as px

# Data for the workflow steps
steps = ["Data Collect", "Feature Eng", "Data Preproc", "Model Dev", 
         "Model Train", "Backtesting", "Performance", "Hypothesis", "Results"]

details = ["Apple 2017-25", "11 Features", "Split + Norm", "SARIMAX+LSTM", 
           "7 Yrs Training", "1 Yr Forecast", "MAE/RMSE/MAPE", "95% CI Tests", "96.5% Accuracy"]

# Create y positions for vertical flow (top to bottom)
y_positions = list(range(len(steps)-1, -1, -1))
x_positions = [0.5] * len(steps)

# Create the figure
fig = go.Figure()

# Add the workflow steps as scatter points with large markers
fig.add_trace(go.Scatter(
    x=x_positions,
    y=y_positions,
    mode='markers+text',
    marker=dict(
        size=80,
        color=['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', 
               '#B4413C', '#964325', '#944454', '#13343B'][:len(steps)],
        symbol='square'
    ),
    text=steps,
    textposition='middle center',
    textfont=dict(size=12, color='white'),
    hovertemplate='<b>%{text}</b><br>%{customdata}<extra></extra>',
    customdata=details,
    showlegend=False
))

# Add arrows between steps using shapes
for i in range(len(steps)-1):
    fig.add_shape(
        type="line",
        x0=0.5, y0=y_positions[i]-0.3,
        x1=0.5, y1=y_positions[i+1]+0.3,
        line=dict(color="#333333", width=3),
    )
    
    # Add arrowhead
    fig.add_shape(
        type="line",
        x0=0.45, y0=y_positions[i+1]+0.35,
        x1=0.5, y1=y_positions[i+1]+0.3,
        line=dict(color="#333333", width=3),
    )
    fig.add_shape(
        type="line",
        x0=0.55, y0=y_positions[i+1]+0.35,
        x1=0.5, y1=y_positions[i+1]+0.3,
        line=dict(color="#333333", width=3),
    )

# Update layout
fig.update_layout(
    title="Stock Forecast Methodology Workflow",
    xaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[-0.5, 1.5]
    ),
    yaxis=dict(
        showgrid=False,
        showticklabels=False,
        zeroline=False,
        range=[-0.5, len(steps)-0.5]
    ),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

fig.update_traces(cliponaxis=False)

# Save the chart
fig.write_image("stock_methodology_flowchart.png")