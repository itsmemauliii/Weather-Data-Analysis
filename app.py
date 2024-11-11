import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# URL of the dataset (you can replace this with any public URL)
url = "https://www.kaggle.com/datasets/prasad22/weather-data"

# Load the dataset directly from the URL
df = pd.read_csv(url)

# Display the data
st.title('Weather Data Analysis')
st.write(df.head())

# Data Analysis and Visualization
st.write("### Temperature Distribution")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df['Temperature_C'], bins=20, kde=True, color='skyblue', ax=ax)
st.pyplot(fig)

# Embedding the dataset directly
data = {
    'Temperature_C': [22, 25, 30, 27, 28, 24, 29, 31],
    'Humidity_pct': [70, 65, 75, 72, 68, 78, 80, 65],
    'Wind_Speed_kmh': [15, 18, 12, 20, 25, 10, 30, 22]
}

df = pd.DataFrame(data)

# Display the data
st.title('Weather Data Analysis')
st.write(df.head())

# Data Analysis and Visualization
st.write("### Temperature Distribution")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df['Temperature_C'], bins=10, kde=True, color='skyblue', ax=ax)
st.pyplot(fig)

# Scatter plot: Temperature vs Humidity
st.write('### Temperature vs Humidity')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='Temperature_C', y='Humidity_pct', data=df, color='orange', ax=ax)
st.pyplot(fig)

# Load a sample dataset from Seaborn
df = sns.load_dataset('tips')

# Display the data
st.title('Tips Dataset Analysis')
st.write(df.head())

# Data Analysis and Visualization
st.write("### Total Bill Distribution")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df['total_bill'], bins=20, kde=True, color='skyblue', ax=ax)
st.pyplot(fig)

# Scatter plot: Total Bill vs. Tip
st.write('### Total Bill vs Tip')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='total_bill', y='tip', data=df, color='orange', ax=ax)
st.pyplot(fig)

from sklearn.datasets import load_iris
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add the target column (species)
df['Species'] = iris.target

# Display the data
st.title('Iris Dataset Analysis')
st.write(df.head())

# Data Analysis and Visualization
st.write("### Sepal Length Distribution")
fig, ax = plt.subplots(figsize=(8, 6))
sns.histplot(df['sepal length (cm)'], bins=20, kde=True, color='skyblue', ax=ax)
st.pyplot(fig)

# Scatter plot: Sepal Length vs. Sepal Width
st.write('### Sepal Length vs Sepal Width')
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', data=df, hue='Species', ax=ax)
st.pyplot(fig)
