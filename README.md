# 🏪 Smart Vending Insights: A Data Analytics Journey

## 💡 Personal Motivation

As someone fascinated by the intersection of consumer behavior and data science, I've always wondered about the hidden patterns in everyday transactions. Vending machines, those ubiquitous dispensers of quick snacks and drinks, seemed like the perfect microcosm to explore. What drives people to choose Soda over Water at 3 PM? Do rainy days really affect snack sales? Can we predict when a machine will run out of Chocolate bars?

This project emerged from my curiosity about these seemingly simple but surprisingly complex business operations. By analyzing three months of vending machine data, I aimed to uncover actionable insights that could help optimize inventory, maximize revenue, and better serve customers.

## 📊 Dataset Overview

**Source**: Simulated vending machine sales data  
**Timeframe**: 3 months (June - September 2025)  
**Records**: 500+ transactions across 5 machines  
**Locations**: Gym, Office, Campus, Mall  

### Key Variables:
- **Products**: Soda, Water, Chips, Chocolate, Muffin, Energy Drink
- **Operational Data**: Stock levels, timestamps, machine locations
- **Environmental Factors**: Temperature, weather conditions
- **Financial Metrics**: Pricing, revenue, transaction volume

## 🛠️ Tools & Technologies

- **Python**: Primary analysis language
- **Pandas**: Data manipulation and cleaning
- **NumPy**: Statistical calculations and inventory optimization
- **Matplotlib/Seaborn**: Data visualization
- **Excel**: Pivot table analysis and business reporting
- **Jupyter Notebook**: Interactive analysis and documentation

## 🔍 Key Findings

### 📈 Revenue Insights
- **Water emerges as the revenue champion**, generating the highest total sales despite its lower price point
- **Machine performance varies significantly**, with some machines generating 25%+ more revenue than others
- **Peak sales occur during traditional break hours** (around 2-3 PM), suggesting strong correlation with work/study schedules

### ⏰ Demand Patterns
- **Clear hourly patterns exist**, with sales clustering around meal times and afternoon breaks
- **Weekday performance differs from weekends**, indicating location-specific customer behavior
- **Weather shows measurable impact** on product selection, though temperature effects are more subtle than expected

### 📦 Inventory Optimization
- **Stock-out risks identified** for high-velocity items during peak periods
- **Safety stock calculations reveal** optimal buffer levels for different machine-product combinations
- **Reorder point analysis suggests** proactive restocking can prevent lost sales opportunities

## 🎯 Actionable Recommendations

### Operational Excellence
- **Prioritize Water inventory** across all machines given its consistent high demand
- **Schedule restocking during off-peak hours** (early morning or late evening) to maximize machine uptime
- **Monitor high-performing machines more closely** as they drive disproportionate revenue

### Strategic Opportunities
- **Test dynamic pricing** for premium products during peak hours when demand is less price-sensitive
- **Consider location-specific product mixes** based on observed customer preferences
- **Implement weather-based inventory adjustments** for seasonal demand fluctuations

### Inventory Management
- **Adopt calculated reorder points** to prevent stockouts while minimizing excess inventory
- **Establish safety stock buffers** particularly for high-velocity products in busy locations
- **Create automated alerts** when stock levels approach critical thresholds

## 🚀 How to Run This Analysis

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn openpyxl jupyter
```

### Running the Analysis
1. **Clone/Download** this repository
2. **Navigate to the project directory**
3. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook notebooks/vending_analysis.ipynb
   ```
4. **Run all cells** to reproduce the complete analysis

### Viewing Excel Analysis
1. **Open** `excel/vending_pivots.xlsx` in Microsoft Excel or Google Sheets
2. **Explore** the pivot tables on different worksheets
3. **Interact** with the data by filtering and sorting

## 📁 Project Structure

```
smart-vending-insights/
│
├── data/
│   └── vending_sales.csv          # Raw dataset
│
├── notebooks/
│   └── vending_analysis.ipynb     # Main analysis notebook
│
├── excel/
│   └── vending_pivots.xlsx        # Pivot table analysis
│
├── outputs/
│   └── vending_analysis_charts.png # Generated visualizations
│
└── README.md                      # This file
```

## 🎨 Sample Visualizations

The analysis generates multiple visualization types:
- **Bar charts** showing product performance rankings
- **Line charts** tracking daily revenue trends by machine
- **Heatmaps** revealing hour-by-product sales patterns
- **Scatter plots** exploring temperature-sales relationships

## 📝 Next Steps & Future Enhancements

- **Expand dataset** to include seasonal variations and holiday effects
- **Incorporate customer demographics** to understand purchasing behavior
- **Add machine maintenance data** to optimize operational schedules  
- **Explore machine learning models** for demand forecasting
- **Develop real-time dashboard** for operational monitoring

## 🤝 Contributing

This project represents my exploration into retail analytics and inventory optimization. If you find interesting patterns or have suggestions for additional analyses, I'd love to hear your thoughts!

---

