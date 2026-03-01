import matplotlib.pyplot as plt

def plot_state_sales(state_sales):
    plt.figure(figsize=(10,5))
    state_sales.head(10).plot(kind="bar")
    plt.title("Top 10 States by Revenue")
    plt.xlabel("State")
    plt.ylabel("Revenue")
    plt.show()


def plot_monthly_sales(monthly_sales):
    plt.figure(figsize=(8,5))
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.show()