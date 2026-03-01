from data_cleaning import load_and_clean_data
from analysis import calculate_kpis, state_wise_sales, category_wise_sales, monthly_sales
from visualization import plot_state_sales, plot_monthly_sales

# Load Data
file_path = "Amazon Sale Report.csv"
df = load_and_clean_data(file_path)

# Calculate KPIs
total_revenue, total_orders, avg_order_value = calculate_kpis(df)

print("\n========== SALES KPIs ==========")
print("Total Revenue:", total_revenue)
print("Total Orders:", total_orders)
print("Average Order Value:", round(avg_order_value, 2))

# Analysis
state_sales = state_wise_sales(df)
category_sales = category_wise_sales(df)
monthly_sales_data = monthly_sales(df)

print("\nTop 5 States:")
print(state_sales.head())

print("\nCategory-wise Sales:")
print(category_sales)

# Visualization
plot_state_sales(state_sales)
plot_monthly_sales(monthly_sales_data)0