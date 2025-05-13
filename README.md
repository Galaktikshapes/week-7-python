Data Analysis and Visualization with Python
Objective

Load and clean data using pandas.

Perform basic data analysis and summary statistics.

Visualize data with different types of plots.

Requirements
Python 3.x

pandas

matplotlib

seaborn

scikit-learn (for built-in datasets like Iris)

Use the following command to install the necessary dependencies:

pip install pandas matplotlib seaborn scikit-learn
Dataset
The dataset used in this project is the Iris dataset. It is a well-known dataset often used in machine learning tutorials and data analysis. It contains data on iris flowers, specifically their measurements: sepal length, sepal width, petal length, and petal width, categorized by species.

Alternatively, you can upload your own CSV dataset for similar analysis.

Steps
1. Load and Explore the Dataset
The dataset is loaded using the load_iris function from scikit-learn.

We inspect the first few rows to understand the structure of the data.

We check the data types of each column and check for missing values.

The dataset is cleaned by dropping any rows with missing values (if any).

2. Perform Basic Data Analysis
Compute basic statistics (mean, median, standard deviation) for numerical columns.

Perform group-by operations (grouping by species) to compute the mean of numerical columns for each group.

3. Data Visualization
A Line Chart is created to visualize trends in sepal length.

A Bar Chart is used to compare the average petal length per species.

A Histogram is generated to understand the distribution of sepal length.

A Scatter Plot shows the relationship between sepal length and petal length.

4. Error Handling
Included error handling for scenarios where the dataset might not load due to file issues (e.g., file not found, empty data).

Sample Visualizations
1. Line Chart: Sepal Length Trend
This line chart visualizes the trend of sepal length over the dataset indices.

2. Bar Chart: Average Petal Length per Species
A bar chart comparing the average petal length of the three species in the Iris dataset.

3. Histogram: Distribution of Sepal Length
The histogram shows the distribution of the sepal length column to help us understand its spread.

4. Scatter Plot: Sepal Length vs Petal Length
A scatter plot that helps us visualize the relationship between the sepal length and petal length, with color coding for different species.
