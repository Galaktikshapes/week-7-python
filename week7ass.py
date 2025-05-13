import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
import numpy as np

# Load the Iris dataset from sklearn (it's a built-in dataset, so no file reading required)
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['species'] = pd.Categorical.from_codes(data.target, data.target_names)

# Check the first few rows of the data to understand its structure
# This helps us verify the data and look for any obvious issues
print(df.head())

# Explore the structure of the dataset further
# This will show us the data types for each column, which helps us ensure everything is in the correct format
print("\nData Types:")
print(df.dtypes)

# Check for missing values in the dataset
# Although Iris dataset is clean, we might still want to do this step in case the data has issues
print("\nMissing Values:")
print(df.isnull().sum())

# If there were any missing values, we'd handle them here (like filling or dropping)
# For now, we'll just drop any missing values (if any)
df = df.dropna()  # Dropping any rows with missing values (though unlikely in the Iris dataset)

# Task 2: Basic Data Analysis - Let's look at basic stats like mean, median, and standard deviation for each numerical column
print("\nBasic Statistics:")
print(df.describe())

# Group by species and calculate the mean of each numerical column
# This helps us understand the differences between species in terms of flower measurements
print("\nMean of numerical columns grouped by species:")
print(df.groupby('species').mean())

# Task 3: Data Visualization
# Create a Line Chart - This isn't time-series data, but we can show a simple line plot to visualize sepal length values
plt.figure(figsize=(10, 6))
plt.plot(df['sepal length (cm)'], label='Sepal Length', color='blue')
plt.title('Sepal Length Trend (Not Time-Series Data)')  # This is just for illustration, not actual trend analysis
plt.xlabel('Index')  # The x-axis represents the index, which is just the row number
plt.ylabel('Sepal Length (cm)')
plt.legend()  # Adds a legend to the plot for clarity
plt.show()

# Bar Chart: Show the average petal length for each species
# This helps compare petal lengths across different species visually
plt.figure(figsize=(10, 6))
avg_petal_length = df.groupby('species')['petal length (cm)'].mean()
avg_petal_length.plot(kind='bar', color='green')  # Bar chart to compare petal length across species
plt.title('Average Petal Length per Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.xticks(rotation=45)  # Rotating the species names for better readability
plt.show()

# Histogram: Check the distribution of sepal length values
# This will help us understand how sepal lengths are spread out in the dataset
plt.figure(figsize=(10, 6))
df['sepal length (cm)'].hist(bins=15, color='orange', edgecolor='black')  # Customizing the histogram appearance
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# Scatter Plot: Visualize the relationship between sepal length and petal length
# This shows how these two measurements correlate with each other
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df, palette='deep')  # Scatter plot with colors for species
plt.title('Relationship between Sepal Length and Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.legend(title='Species')  # Adding a legend to distinguish between species
plt.show()

# Error Handling: Let's handle cases where the dataset might not be found
# In real-world situations, we might read data from a CSV file, so we include this error handling
try:
    df = pd.read_csv('your_dataset.csv')  # Replace with actual path if loading from file
except FileNotFoundError:
    print("Error: The file was not found. Make sure the path is correct.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty. Please provide a valid file with data.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
