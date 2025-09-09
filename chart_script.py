import plotly.graph_objects as go
import plotly.io as pio

# Data from the provided JSON
products = ["Water", "Soda", "Chips", "Chocolate", "Energy Drink", "Muffin"]
revenue = [387.5, 295.0, 228.0, 146.0, 122.5, 96.0]

# Brand colors in specified order
colors = ['#1FB8CD', '#DB4545', '#2E8B57', '#5D878F', '#D2BA4C', '#B4413C']

# Create bar chart
fig = go.Figure(data=[
    go.Bar(
        x=products,
        y=revenue,
        marker_color=colors[:len(products)],
        name='Revenue'
    )
])

# Update traces
fig.update_traces(cliponaxis=False)

# Update layout with title and axis labels
fig.update_layout(
    title="Revenue by Product",
    xaxis_title="Products",
    yaxis_title="Revenue ($)",
    showlegend=False  # No need for legend since it's a single series
)

# Update axes formatting
fig.update_yaxes(tickformat="$,.0f")

# Save the chart
fig.write_image("revenue_by_product_chart.png")