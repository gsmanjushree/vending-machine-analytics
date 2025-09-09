import plotly.graph_objects as go
import pandas as pd

# Data
data = {
    "dates": ["2025-06-12", "2025-06-13", "2025-06-14", "2025-06-15", "2025-06-16", "2025-06-17", "2025-06-18", "2025-06-19", "2025-06-20", "2025-06-21"], 
    "M01": [45.5, 32.0, 28.5, 51.0, 38.5, 42.0, 35.5, 29.0, 47.5, 33.0], 
    "M02": [38.0, 29.5, 45.5, 31.0, 42.5, 28.0, 51.5, 36.0, 25.5, 48.0], 
    "M03": [52.0, 41.5, 33.0, 28.5, 45.0, 39.5, 31.0, 54.5, 42.0, 27.5], 
    "M04": [31.5, 48.0, 39.5, 42.0, 29.5, 51.0, 44.5, 33.0, 38.5, 46.0], 
    "M05": [42.0, 35.5, 48.5, 33.0, 51.5, 38.0, 29.5, 45.0, 31.5, 52.0]
}

# Colors in order
colors = ["#1FB8CD", "#DB4545", "#2E8B57", "#5D878F", "#D2BA4C"]

# Create figure
fig = go.Figure()

# Add traces for each machine
machines = ["M01", "M02", "M03", "M04", "M05"]
for i, machine in enumerate(machines):
    fig.add_trace(go.Scatter(
        x=data["dates"],
        y=data[machine],
        mode='lines',
        name=machine,
        line=dict(color=colors[i])
    ))

# Update traces
fig.update_traces(cliponaxis=False)

# Update layout
fig.update_layout(
    title="Vending Machine Revenue Trends",
    xaxis_title="Date",
    yaxis_title="Revenue ($)",
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# Save the chart
fig.write_image("vending_revenue_trends.png")