import pandas as pd

# Load the dataset
df = pd.read_csv('repositories.csv')

# Display the first few rows of the dataset
df.head()

# Get information about the dataset
df.info()

# Summarize statistics of numerical columns
df.describe()

# Find the Repository with the Most Stars:
most_stars_repo = df[df['Stars'] == df['Stars'].max()]
print("Repository with the most stars:")
print(most_stars_repo)

# Calculate the Mean and Median Number of Stars:
mean_stars = df['Stars'].mean()
median_stars = df['Stars'].median()
print(f"Mean Stars: {mean_stars}")
print(f"Median Stars: {median_stars}")

# Visualize the Number of Stars Using a Histogram:
import matplotlib.pyplot as plt

plt.hist(df['Stars'], bins=20)
plt.xlabel('Stars')
plt.ylabel('Frequency')
plt.title('Distribution of Stars')
plt.show()
