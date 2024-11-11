import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/kaggle/input/weather-data/weather_data.csv')

# Title of the app
st.title('Weather Data Analysis')

# Display first few rows of the dataset
st.write('### Dataset Overview')
st.dataframe(df.head())

# Show basic statistics
st.write('### Basic Statistics')
st.write(df.describe())

# Temperature Distribution
st.write('### Temperature Distribution')
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df['Temperature_C'], bins=20, kde=True, color='skyblue', ax=ax)
st.pyplot(fig)

# Scatter plot: Temperature vs Humidity
st.write('### Temperature vs Humidity')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='Temperature_C', y='Humidity_pct', data=df, color='orange', ax=ax)
st.pyplot(fig)

# Scatter plot: Wind Speed vs Temperature
st.write('### Wind Speed vs Temperature')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='Wind_Speed_kmh', y='Temperature_C', data=df, color='green', ax=ax)
st.pyplot(fig)
