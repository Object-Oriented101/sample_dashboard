import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set the title
st.title("Operations KPI Dashboard")

# Generate mock data
np.random.seed(42)
dates = pd.date_range("2025-01-01", "2025-05-11")
data = {
    "Date": np.random.choice(dates, 100),
    "Leads": np.random.randint(50, 200, 100),
    "Sales": np.random.randint(10, 50, 100),
    "Conversion Rate (%)": np.random.uniform(10, 30, 100).round(2),
    "Revenue": np.random.randint(1000, 5000, 100),
}
df = pd.DataFrame(data)

# Display the data
st.subheader("Raw Data")
st.dataframe(df)

# KPI calculations
total_revenue = df["Revenue"].sum()
total_sales = df["Sales"].sum()
average_conversion = df["Conversion Rate (%)"].mean().round(2)

# Display KPIs
st.subheader("Key Performance Indicators")
st.metric("Total Revenue", f"${total_revenue}")
st.metric("Total Sales", total_sales)
st.metric("Average Conversion Rate", f"{average_conversion}%")

# Plotting a simple sales trend
st.subheader("Sales Trend Over Time")
sales_trend = df.groupby("Date").sum().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(sales_trend.index, sales_trend["Sales"], marker='o', linestyle='-')
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.grid(True)
st.pyplot(plt)

# Revenue Distribution
st.subheader("Revenue Distribution")
plt.figure(figsize=(8, 6))
plt.hist(df["Revenue"], bins=15, color='skyblue', edgecolor='black')
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.grid(True)
st.pyplot(plt)

# Filter by date
st.subheader("Filter Data by Date Range")
start_date = st.date_input("Start Date", value=pd.to_datetime("2025-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2025-05-11"))
filtered_df = df[(df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Operations Metrics Section
st.subheader("Operations Metrics")

team_members = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
operations_data = {
    "Team Member": team_members,
    "Tasks Completed (Monthly)": np.random.randint(5, 15, len(team_members)),
    "Average Days per Task": np.random.uniform(3, 7, len(team_members)).round(2),
    "Projects Completed (Monthly)": np.random.randint(2, 8, len(team_members)),
    "Late Projects": np.random.randint(0, 3, len(team_members)),
    "Task Efficiency (%)": np.random.uniform(70, 95, len(team_members)).round(2),
}
operations_df = pd.DataFrame(operations_data)

st.dataframe(operations_df)

# Additional Operations Metrics (non-grid format)
st.subheader("Additional Operations Metrics")

average_task_completion_time = operations_df["Average Days per Task"].mean().round(2)
late_project_rate = (operations_df["Late Projects"].sum() / operations_df["Projects Completed (Monthly)"].sum() * 100).round(2)

st.write(f"**Average Task Completion Time:** {average_task_completion_time} days")
st.write(f"**Total Projects Completed:** {operations_df['Projects Completed (Monthly)'].sum()}")
st.write(f"**Late Project Rate:** {late_project_rate}%")
st.write(f"**Total Tasks Completed:** {operations_df['Tasks Completed (Monthly)'].sum()}")
st.write(f"**Overall Task Efficiency:** {operations_df['Task Efficiency (%)'].mean().round(2)}%")
