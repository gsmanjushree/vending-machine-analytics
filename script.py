import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate vending machine sales data
def generate_vending_data(n_rows=500):
    # Base parameters
    machines = ['M01', 'M02', 'M03', 'M04', 'M05']
    locations = ['Gym', 'Office', 'Campus', 'Mall']
    products = ['Soda', 'Water', 'Chips', 'Chocolate', 'Muffin', 'Energy Drink']
    categories = {'Soda': 'Drink', 'Water': 'Drink', 'Energy Drink': 'Drink', 
                  'Chips': 'Food', 'Chocolate': 'Food', 'Muffin': 'Food'}
    
    # Product prices
    prices = {'Soda': 2.50, 'Water': 1.50, 'Chips': 3.00, 
              'Chocolate': 2.00, 'Muffin': 4.00, 'Energy Drink': 3.50}
    
    # Start date (3 months ago)
    start_date = datetime.now() - timedelta(days=90)
    
    data = []
    machine_stocks = {machine: {product: 50 for product in products} for machine in machines}
    
    for i in range(n_rows):
        # Generate timestamp (weighted towards business hours)
        days_offset = random.randint(0, 89)
        if random.random() < 0.7:  # 70% business hours
            hour = random.choices(range(6, 22), weights=[1,2,3,5,8,10,12,15,12,10,8,5,3,2,1,1])[0]
        else:
            hour = random.randint(0, 23)
        
        timestamp = start_date + timedelta(days=days_offset, hours=hour, 
                                          minutes=random.randint(0, 59))
        
        # Select machine and location
        machine = random.choice(machines)
        location = random.choice(locations)
        
        # Select product (some products more popular)
        product_weights = {'Soda': 25, 'Water': 30, 'Chips': 20, 
                          'Chocolate': 15, 'Muffin': 5, 'Energy Drink': 5}
        product = random.choices(products, weights=list(product_weights.values()))[0]
        
        # Quantity (usually 1, sometimes 2)
        quantity = random.choices([1, 2], weights=[80, 20])[0]
        
        # Check if restock needed (random restocking events)
        if machine_stocks[machine][product] < quantity or random.random() < 0.02:
            machine_stocks[machine][product] = random.randint(40, 60)  # Restock
        
        stock_before = machine_stocks[machine][product]
        stock_after = max(0, stock_before - quantity)
        machine_stocks[machine][product] = stock_after
        
        # Skip if no stock
        if stock_before < quantity:
            continue
            
        # Weather data
        temperature = np.random.normal(22, 8)  # Average 22°C with variation
        rain = random.choices([0, 1], weights=[75, 25])[0]  # 25% chance of rain
        
        data.append({
            'sale_id': f'S{i+1:04d}',
            'machine_id': machine,
            'location_type': location,
            'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'product': product,
            'category': categories[product],
            'price': prices[product],
            'quantity': quantity,
            'stock_before': stock_before,
            'stock_after': stock_after,
            'temperature_c': round(temperature, 1),
            'rain': rain
        })
    
    return pd.DataFrame(data)

# Generate the dataset
df = generate_vending_data(500)

# Display basic info about the dataset
print(f"Dataset generated with {len(df)} rows")
print(f"Date range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"\nFirst 10 rows:")
print(df.head(10))

# Save the dataset
df.to_csv('vending_sales.csv', index=False)
print("\nDataset saved as 'vending_sales.csv'")