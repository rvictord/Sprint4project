import streamlit as st
import pandas as pd
import plotly.express as px 
# Load data
data = pd.read_csv(r'C:\Users\victo\OneDrive\Documents\GitHub\Sprint4project\vehicles_us.csv', encoding='utf-8')

# Header
st.header("Exploratory Data Analysis")
# Checkbox to toggle between histograms and scatter plots
show_histograms = st.checkbox("Show histograms", True)
# Histogram of mileage
if show_histograms:
    st.subheader("Mileage Distribution")
    fig = px.histogram(data, x="odometer")
    st.plotly_chart(fig)
# Show scatter plot of days listed vs condition
show_days_vs_condition = st.checkbox("Show days listed vs condition scatter plot")
if show_days_vs_condition:
    st.subheader("Days Listed vs Condition")
    fig = px.scatter(data, x="days_listed", y="condition")
    st.plotly_chart(fig)
# Scatter plot of mileage vs. price
st.subheader("Mileage vs. Price")
fig = px.scatter(data, x="odometer", y="price")
st.plotly_chart(fig)
