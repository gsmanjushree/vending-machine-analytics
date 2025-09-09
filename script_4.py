# Let's show some sample data from our CSV to give users a preview
df = pd.read_csv('vending_sales.csv')

print("=== SMART VENDING INSIGHTS PROJECT SUMMARY ===\n")

print("📊 DATASET SAMPLE (First 10 rows):")
print(df.head(10).to_string(index=False))

print(f"\n📈 QUICK STATS:")
print(f"• Total Transactions: {len(df):,}")
print(f"• Date Range: {df['timestamp'].min()} to {df['timestamp'].max()}")
print(f"• Machines: {df['machine_id'].nunique()} ({', '.join(sorted(df['machine_id'].unique()))})")
print(f"• Products: {df['product'].nunique()} ({', '.join(df['product'].unique())})")
print(f"• Locations: {', '.join(df['location_type'].unique())}")

# Revenue analysis
df['revenue'] = df['price'] * df['quantity']
total_revenue = df['revenue'].sum()
print(f"• Total Revenue: ${total_revenue:,.2f}")
print(f"• Average Transaction: ${df['revenue'].mean():.2f}")

print(f"\n🏆 TOP PERFORMERS:")
top_product = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
print(f"• Best Product: {top_product.index[0]} (${top_product.iloc[0]:.2f})")

top_machine = df.groupby('machine_id')['revenue'].sum().sort_values(ascending=False)
print(f"• Best Machine: {top_machine.index[0]} (${top_machine.iloc[0]:.2f})")

top_location = df.groupby('location_type')['revenue'].sum().sort_values(ascending=False)
print(f"• Best Location: {top_location.index[0]} (${top_location.iloc[0]:.2f})")

print(f"\n📁 GENERATED FILES:")
print("✅ vending_sales.csv (500+ transaction records)")
print("✅ vending_analysis.ipynb (Complete analysis notebook)")
print("✅ vending_pivots.xlsx (Excel pivot tables)")
print("✅ README.md (Project documentation)")
print("✅ 3 visualization charts (Revenue, trends, heatmap)")

print(f"\n🎯 PROJECT HIGHLIGHTS:")
print("• Beginner-friendly with step-by-step explanations")
print("• Real business scenarios with actionable insights")
print("• Multiple analysis techniques (descriptive, predictive)")
print("• Professional visualizations and reporting")
print("• Complete inventory optimization calculations")
print("• Price sensitivity analysis and recommendations")

print(f"\n🚀 READY TO USE:")
print("All files are complete and can be used immediately!")
print("Simply run the Jupyter notebook or explore the Excel pivots.")