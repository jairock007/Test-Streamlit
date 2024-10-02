import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('github_dataset.csv')

st.title('GitHub Repositories Dashboard')
st.write("This dashboard provides insights into GitHub repositories dataset.")

# st.write(df.columns)  # This will display all column names in the dataset


# Example: Show the top 10 most popular repositories
top_repos = df.nlargest(10, 'stars_count')
st.bar_chart(top_repos[['repositories', 'stars_count']].set_index('repositories'))