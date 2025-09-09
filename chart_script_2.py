import plotly.graph_objects as go
import plotly.io as pio

# Data from the provided JSON
hours = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
products = ["Water", "Soda", "Chips", "Chocolate", "Energy Drink", "Muffin"]
sales_matrix = [[2, 1, 1, 1, 0, 0], [5, 3, 2, 2, 1, 1], [8, 6, 4, 3, 2, 1], [12, 8, 6, 4, 3, 2], [10, 7, 5, 4, 2, 1], [15, 10, 8, 6, 4, 3], [18, 12, 10, 8, 5, 4], [20, 15, 12, 9, 6, 5], [22, 18, 14, 11, 7, 6], [25, 20, 16, 12, 8, 7], [18, 14, 11, 9, 6, 4], [15, 12, 9, 7, 5, 3], [12, 9, 7, 5, 4, 2], [8, 6, 5, 3, 2, 1], [5, 4, 3, 2, 1, 1], [3, 2, 2, 1, 1, 0]]

# Format hours for display (keeping under 15 character limit)
hour_labels = [f"{h}:00" for h in hours]

# Create heatmap
fig = go.Figure(data=go.Heatmap(
    z=sales_matrix,
    x=products,
    y=hour_labels,
    colorscale='Blues',
    showscale=True,
    colorbar=dict(title="Sales Volume"),
    hovertemplate='Hour: %{y}<br>Product: %{x}<br>Sales: %{z}<extra></extra>'
))

# Update layout with proper labels
fig.update_layout(
    title="Sales by Hour & Product",
    xaxis_title="Product",
    yaxis_title="Hour"
)

# Save the chart as PNG
fig.write_image("sales_heatmap.png")