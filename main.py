import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('github_dataset.csv')

# Strip whitespace from columns and check column names
df.columns = df.columns.str.strip()
st.write("Dataset Columns:", df.columns)

# Top 10 Most Starred Repositories
st.header("Top 10 Most Starred Repositories")
top_repos = df.nlargest(10, 'stars_count')
plt.figure(figsize=(10, 5))
sns.barplot(x=top_repos['repositories'], y=top_repos['stars_count'], palette='viridis')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.title('Top 10 Repositories by stars_count')
plt.xlabel('Repository Name')
plt.ylabel('stars_count')
st.pyplot(plt)

# Repositories by Programming Language
st.header("Repositories by Programming Language")
language_counts = df['language'].value_counts().nlargest(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=language_counts.index, y=language_counts.values, palette='magma')
plt.xticks(rotation=45, ha='right')
plt.title('Top 10 Languages by Number of Repositories')
plt.xlabel('Programming Language')
plt.ylabel('Count')
st.pyplot(plt)

# Relationship between stars_count and forks_count
st.header("Correlation Between stars_count and forks_count")
plt.figure(figsize=(10, 5))
sns.scatterplot(x=df['stars_count'], y=df['forks_count'], alpha=0.6)
plt.title('stars_count vs forks_count')
plt.xlabel('stars_count')
plt.ylabel('forks_count')
st.pyplot(plt)

# Display data table for users to explore
st.header("Explore the Dataset")
st.write(df)
