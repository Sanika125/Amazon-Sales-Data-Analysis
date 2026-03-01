def calculate_kpis(df):
    total_revenue = df["Amount"].sum()
    total_orders = df["Order ID"].nunique()
    avg_order_value = total_revenue / total_orders

    return total_revenue, total_orders, avg_order_value


def state_wise_sales(df):
    return df.groupby("ship-state")["Amount"].sum().sort_values(ascending=False)


def category_wise_sales(df):
    return df.groupby("Category")["Amount"].sum().sort_values(ascending=False)


def monthly_sales(df):
    df["Month"] = df["Date"].dt.month
    return df.groupby("Month")["Amount"].sum()