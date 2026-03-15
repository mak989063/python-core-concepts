import streamlit as st
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
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

future = pd.DataFrame({"day":[8,9,10,11,12]})

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

#BillDataImport
st.subheader("Billit Data Import")

uploaded_file = st.file_uploader("Upload Billit Sales CSV")

if uploaded_file:

    billit_df = pd.read_csv(uploaded_file)

    st.write("Raw Billit Data")
    st.dataframe(billit_df)

    # Example assumption
    if "amount" in billit_df.columns:

        total_sales = billit_df["amount"].sum()

        total_orders = len(billit_df)

        avg_order = total_sales / total_orders

        st.write("Total Sales ₹", total_sales)

        st.write("Total Orders", total_orders)

        st.write("Average Order Value ₹", round(avg_order))


#Menu Price Optimizer
st.subheader("Menu Price Optimizer")

target_margin = st.slider("Target Profit Margin %",20,80,40)

df["Recommended_price"] = df["Cost"] / (1 - target_margin/100)

df["Recommended_price"] = df["Recommended_price"].round()

optimizer_df = df[["Item","Cost","Price","Recommended_price"]]

st.dataframe(optimizer_df)

fig5, ax5 = plt.subplots()

ax5.bar(optimizer_df["Item"], optimizer_df["Recommended_price"])

ax5.set_title("Recommended Menu Price")

st.pyplot(fig5)

#Customer Demand Prediction
st.subheader("Customer Demand Prediction")

demand_data = {
    "day":[1,2,3,4,5,6,7],
    "porotta":[120,130,140,110,125,135,150],
    "chicken":[35,40,38,30,33,36,41],
    "beef":[45,48,50,42,44,46,52]
}

demand_df = pd.DataFrame(demand_data)

st.dataframe(demand_df)

# Training input
X = demand_df[["day"]]

# Future days to predict
future_days = pd.DataFrame({"day":[8,9,10]})

for item in ["porotta","chicken","beef"]:

    y = demand_df[item]

    model = LinearRegression()

    model.fit(X, y)

    prediction = model.predict(future_days)

    pred_df = pd.DataFrame({
        "Day":[8,9,10],
        "Predicted Demand":prediction.round()
    })

    st.write(item.upper(),"Demand Forecast")

    st.dataframe(pred_df)