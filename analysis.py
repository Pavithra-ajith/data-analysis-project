import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("titanic.csv")

# See first 5 rows
print("First 5 rows of dataset:")
print(df.head())

# How many passengers survived
print("Total survived:", df['Survived'].sum())

# Average age of passengers
print("Average Age:", df['Age'].mean())

# Gender count plot
df['Sex'].value_counts().plot(kind='bar')
plt.title("Passengers by Gender")
plt.show()
