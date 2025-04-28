# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 21:47:46 2025

@author: zulfi
"""

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset (correct file name)
df = pd.read_csv('../data/WHR2024.csv')

# Displaying the first 5 rows of the dataset
print(df.head())

# Getting general information about the dataset (columns, data types, non-null counts)
print(df.info())

# Checking for missing values in each column
print(df.isnull().sum())

# Finding the top 10 happiest countries
top_10_happiest = df.sort_values(by='Ladder score', ascending=False).head(10)
print(top_10_happiest[['Country name', 'Ladder score']])

# Plotting a nicer bar chart for the top 10 happiest countries
plt.figure(figsize=(12,7))

bars = plt.bar(top_10_happiest['Country name'], top_10_happiest['Ladder score'])

# Adding color to bars
for bar in bars:
    bar.set_color('skyblue')

# Adding gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding title and labels with bigger font sizes
plt.title('Top 10 Happiest Countries (2024)', fontsize=18)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Ladder Score', fontsize=14)

# Rotating x-axis labels
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Adding values on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.2f}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=10)

# Making layout tight
plt.tight_layout()

# Saving the figure
plt.savefig('../images/top_10_happiest_countries.png')

# Showing the plot
plt.show()


# Finding the bottom 10 countries (least happy)
bottom_10_unhappiest = df.sort_values(by='Ladder score', ascending=True).head(10)
print(bottom_10_unhappiest[['Country name', 'Ladder score']])


# Plotting a nicer bar chart for the bottom 10 happiest countries
plt.figure(figsize=(12,7))

bars = plt.bar(bottom_10_unhappiest['Country name'], bottom_10_unhappiest['Ladder score'], color='lightcoral')

# Adding gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding title and labels with bigger font sizes
plt.title('Bottom 10 Least Happy Countries (2024)', fontsize=18)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Ladder Score', fontsize=14)

# Rotating x-axis labels
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(fontsize=12)

# Adding values on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.annotate(f'{height:.2f}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom', fontsize=10)

# Making layout tight
plt.tight_layout()

# Saving the figure
plt.savefig('../images/bottom_10_unhappiest_countries.png')

# Showing the plot
plt.show()


# Scatter Plot: GDP per capita vs Ladder score

plt.figure(figsize=(10,6))

plt.scatter(df['Explained by: Log GDP per capita'], df['Ladder score'], color='mediumseagreen', edgecolors='black')

plt.title('GDP per Capita vs Happiness Score (2024)', fontsize=18)
plt.xlabel('Log GDP per Capita', fontsize=14)
plt.ylabel('Ladder Score', fontsize=14)

plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()

plt.savefig('../images/gdp_vs_happiness_scatter.png')
plt.show()

