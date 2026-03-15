# Kitchen Mates Business Analytics Dashboard

A **Streamlit-powered restaurant analytics dashboard** designed to analyze business performance, predict sales, optimize menu pricing, and simulate profitability for small restaurant businesses.

This project was built using **real-world restaurant sales insights** from Kitchen Mates to help restaurant owners make **data-driven decisions**.

---

# Overview

Running a restaurant involves balancing many factors such as:

* Daily sales
* Staff expenses
* Raw material costs
* Menu pricing
* Customer demand

This dashboard provides a **data analytics tool** that helps restaurant owners:

* Understand profitability
* Predict sales
* Optimize menu pricing
* Forecast demand
* Simulate business scenarios

---

# Features

## 1. Daily Financial Analysis

Displays real-time business health including:

* Daily sales
* Daily expenses
* Profit or loss

Helps determine whether the restaurant is **operating profitably**.

---

## 2. Break-Even Analysis

Calculates the **minimum daily sales required** to cover expenses.

Includes a graph showing:

Daily Sales vs Profit

This helps answer:

How much should the restaurant sell each day to survive?

---

## 3. Average Order Value Simulation

Simulates profitability based on:

* Average order value
* Number of orders per day

Example:

Average Order Value = ₹230
Orders per day = 100

Daily Sales = ₹23,000

This module shows how **increasing order value improves profitability**.

---

## 4. Menu Profit Analysis

Analyzes each menu item based on:

* Selling price
* Food cost
* Quantity sold

Calculates:

* Profit per item
* Total profit contribution

Helps identify **high-margin menu items**.

---

## 5. Menu Price Optimizer

Suggests recommended prices based on a **target profit margin**.

Example:

Food Cost = ₹75
Target Margin = 40%

Recommended Price = ₹125

This ensures menu pricing supports sustainable profit margins.

---

## 6. Customer Demand Prediction

Uses **Machine Learning (Linear Regression)** to predict future demand for popular items such as:

* Porotta
* Chicken
* Beef

Helps plan:

* Ingredient purchases
* Food preparation
* Staff requirements

---

## 7. Sales Forecasting

Predicts future sales trends using historical sales data.

This allows restaurant owners to anticipate:

* High-demand days
* Slow periods
* Revenue trends

---

## 8. Staff Cost Optimization

Simulates daily expenses based on different staff counts.

Helps answer:

How many employees should the restaurant have to remain profitable?

---

## 9. Billit CSV Data Import

The dashboard can analyze **real restaurant sales data** exported from the Billit POS system.

Example CSV format:

date,item,qty,amount
2026-03-01,Bun Porotta,2,60
2026-03-01,Beef Chukka,1,130
2026-03-01,Porotta,3,54

The system calculates:

* Total sales
* Total orders
* Average order value

---

# Technology Stack

Python
Streamlit
Pandas
NumPy
Matplotlib
Scikit-learn

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/kitchen-mates-analytics.git
```

Navigate into the project directory:

```
cd kitchen-mates-analytics
```

Install dependencies:

```
pip install streamlit pandas numpy matplotlib scikit-learn
```

---

# Running the Application

Run the Streamlit app:

```
streamlit run business_analysis.py
```

Open the dashboard in your browser:

```
http://localhost:8501
```

---

# Example Use Case

Restaurant owners can use this dashboard to answer questions like:

* How many orders per day are required to break even?
* What menu items generate the most profit?
* What should be the optimal price for each item?
* How will increasing average order value impact profit?
* How much food should be prepared tomorrow?

---

# Future Improvements

Planned enhancements include:

* Combo recommendation engine
* Ingredient demand forecasting
* Inventory cost optimization
* Ramzan and weekend sales forecasting
* Interactive Plotly dashboards
* AI-driven pricing strategy

---

# Author

Manikandan Krishnamoorthi

Restaurant owner and software enthusiast building data-driven tools for small businesses.

---

# License

This project is open-source and available under the MIT License.
