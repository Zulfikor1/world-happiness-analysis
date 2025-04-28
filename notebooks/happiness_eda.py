# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 21:47:46 2025

@author: zulfi
"""

# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  # For trend line (regression line)

# Reading the dataset
df = pd.read_csv('../data/WHR2024.csv')

# Displaying the first 5 rows of the dataset
print(df.head())

# Getting general information about the dataset
print(df.info())

# Checking for missing values
print(df.isnull().sum())

# Removing rows with missing values in the relevant columns
df_clean = df.dropna(subset=['Explained by: Log GDP per capita', 'Ladder score'])

# Finding the top 10 happiest countries
top_10_happiest = df_clean.sort_values(by='Ladder score', ascending=False).head(10)
print(top_10_happiest[['Country name', 'Ladder score']])

# Plotting the bar chart for top 10 happiest countries
plt.figure(figsize=(12,7))
bars = plt.bar(top_10_happiest['Country name'], top_10_happiest['Ladder score'])

# Adding color to bars
for bar in bars:
    bar.set_color('skyblue')

# Adding gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding title and labels
plt.title('Top 10 Happiest Countries (2024)', fontsize=18)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Ladder Score', fontsize=14)

# Rotating x-axis labels for readability
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

# Tightening layout
plt.tight_layout()

# Saving the figure
plt.savefig('../images/top_10_happiest_countries.png')

# Showing the plot
plt.show()


# Finding the bottom 10 least happy countries
bottom_10_unhappiest = df_clean.sort_values(by='Ladder score', ascending=True).head(10)
print(bottom_10_unhappiest[['Country name', 'Ladder score']])


# Plotting the bar chart for the bottom 10 least happy countries
plt.figure(figsize=(12,7))
bars = plt.bar(bottom_10_unhappiest['Country name'], bottom_10_unhappiest['Ladder score'], color='lightcoral')

# Adding gridlines
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding title and labels
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

# Tightening layout
plt.tight_layout()

# Saving the figure
plt.savefig('../images/bottom_10_unhappiest_countries.png')

# Showing the plot
plt.show()


# Scatter Plot: GDP per capita vs Ladder score

plt.figure(figsize=(10,6))

# Scatter plot for GDP vs Happiness
plt.scatter(df_clean['Explained by: Log GDP per capita'], df_clean['Ladder score'], color='mediumseagreen', edgecolors='black')

# Adding trend line (regression line)
z = np.polyfit(df_clean['Explained by: Log GDP per capita'], df_clean['Ladder score'], 1)  # Linear regression (degree 1)
p = np.poly1d(z)

plt.plot(df_clean['Explained by: Log GDP per capita'], p(df_clean['Explained by: Log GDP per capita']), color='red', linewidth=2, label='Trend Line')

# Adding title and labels
plt.title('GDP per Capita vs Happiness Score (2024)', fontsize=18)
plt.xlabel('Log GDP per Capita', fontsize=14)
plt.ylabel('Ladder Score', fontsize=14)

# Adding gridlines
plt.grid(True, linestyle='--', alpha=0.7)

# Adding legend
plt.legend()

# Tightening layout
plt.tight_layout()

# Saving the figure
plt.savefig('../images/gdp_vs_happiness_scatter_with_trendline.png')

# Showing the plot
plt.show()
