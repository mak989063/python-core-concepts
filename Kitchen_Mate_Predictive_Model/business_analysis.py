import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("Kitchen Mates Business Analytics Dashboard")

st.sidebar.header("Business Inputs")

rent = st.sidebar.number_input("Monthly Rent", value=32000)
employees = st.sidebar.number_input("Employees", value=7)
salary = st.sidebar.number_input("Salary per Employee", value=12000)
raw_material = st.sidebar.number_input("Raw Material Cost per Day", value=5000)
utilities = st.sidebar.number_input("Gas + Electricity per Day", value=2000)

daily_sales = st.sidebar.number_input("Average Daily Sales", value=9500)

# Expense calculation
rent_daily = rent / 30
salary_daily = (employees * salary) / 30

daily_expense = rent_daily + salary_daily + raw_material + utilities

profit = daily_sales - daily_expense

st.subheader("Daily Financial Status")

col1, col2, col3 = st.columns(3)

col1.metric("Daily Sales", f"₹{daily_sales}")
col2.metric("Daily Expense", f"₹{round(daily_expense)}")
col3.metric("Profit / Loss", f"₹{round(profit)}")

# Break-even
st.subheader("Break Even Analysis")

sales_range = np.arange(5000, 50000, 1000)
profit_range = sales_range - daily_expense

fig, ax = plt.subplots()

ax.plot(sales_range, profit_range)
ax.axhline(0)
ax.set_xlabel("Daily Sales")
ax.set_ylabel("Profit")

st.pyplot(fig)

st.write("Break-even sales:", round(daily_expense))

# Restructured Menu profit analysis
st.subheader("Restructured Menu Profit Analysis")

menu = {
    "Item": ["Bun Porotta", "Porotta", "Beef Chukka", "Chicken Kothu",
             "Pepper Chicken","Chilli Chicken","Mutton Chukka"],
    "Price": [30, 18, 130, 170, 150,150, 210],
    "Cost": [10, 6, 75, 95, 85,85,120],
    "Qty": [752, 373, 52, 26, 20,20,9]
}

df = pd.DataFrame(menu)

df["Profit_per_item"] = df["Price"] - df["Cost"]
df["Total_profit"] = df["Profit_per_item"] * df["Qty"]

st.dataframe(df)

fig2, ax2 = plt.subplots()

ax2.bar(df["Item"], df["Total_profit"])

st.pyplot(fig2)

# Sales forecasting

st.subheader("Sales Forecast (Future Model Prediction)")

days = np.array([1, 2, 3, 4, 5, 6, 7]).reshape(-1, 1)
sales = np.array([9200, 9800, 10100, 8900, 9400, 9700, 9600])

model = LinearRegression()
model.fit(days, sales)

future = np.array([[8], [9], [10], [11], [12]])

prediction = model.predict(future)

forecast_df = pd.DataFrame({
    "Day": [8, 9, 10, 11, 12],
    "Predicted Sales": prediction
})

st.dataframe(forecast_df)

fig3, ax3 = plt.subplots()

ax3.plot(days, sales, label="Past")
ax3.plot(future, prediction, label="Prediction")

ax3.legend()

st.pyplot(fig3)

st.subheader("Staff Optimization")

staff_options = []

for s in range(3, 8):
    salary_cost = (s * salary) / 30
    expense = rent_daily + salary_cost + raw_material + utilities

    staff_options.append([s, round(expense)])

staff_df = pd.DataFrame(staff_options, columns=["Employees", "Daily Expense"])

st.dataframe(staff_df)

# Average Order Value Simulation

st.subheader("Average Order Value Simulation")

orders = st.slider("Orders per Day", 20, 200, 80)

avg_order_value = st.number_input("Average Order Value (₹)", value=230)

simulated_sales = orders * avg_order_value

simulated_profit = simulated_sales - daily_expense

col1, col2, col3 = st.columns(3)

col1.metric("Simulated Daily Sales", f"₹{simulated_sales}")
col2.metric("Daily Expense", f"₹{round(daily_expense)}")
col3.metric("Projected Profit", f"₹{round(simulated_profit)}")

st.write("Orders needed to break even:")

orders_break_even = daily_expense / avg_order_value

st.write(round(orders_break_even), "orders/day")

# Order simulation graph

orders_range = np.arange(20, 200, 10)

sales_projection = orders_range * avg_order_value

profit_projection = sales_projection - daily_expense

fig4, ax4 = plt.subplots()

ax4.plot(orders_range, profit_projection)

ax4.axhline(0)

ax4.set_xlabel("Orders per Day")

ax4.set_ylabel("Profit")

ax4.set_title("Orders vs Profit Simulation")

st.pyplot(fig4)