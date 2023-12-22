# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:48:05 2023

@author: Danille
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel sheet
excel_path = 'C:/Users/Danille/Desktop/Gebied_07/CSV/TBL_Sporen.xlsx'
df = pd.read_excel(excel_path)

# Display available columns to the user
available_columns = df.columns.tolist()
print("Available columns:", available_columns)

# Function to create bar charts for selected columns
def create_bar_charts(df, selected_columns):
    for i in range(len(selected_columns)):
        for j in range(i + 1, len(selected_columns)):
            plt.figure(figsize=(10, 6))
            sns.countplot(x=selected_columns[i], hue=selected_columns[j], data=df)
            plt.title(f'Bar Chart of {selected_columns[i]} vs {selected_columns[j]}')
            plt.xlabel(selected_columns[i])
            plt.ylabel('Count')
            plt.legend(title=selected_columns[j])
            plt.show()

# Function to create scatter plots for selected columns
def create_scatter_plots(df, selected_columns):
    for i in range(len(selected_columns)):
        for j in range(i + 1, len(selected_columns)):
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=selected_columns[i], y=selected_columns[j], data=df)
            plt.title(f'Scatter Plot of {selected_columns[i]} vs {selected_columns[j]}')
            plt.xlabel(selected_columns[i])
            plt.ylabel(selected_columns[j])
            plt.show()

# Function to create histograms for selected columns
def create_histograms(df, selected_columns):
    for column in selected_columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], bins=20, kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

# Function to create pie charts for selected columns
def create_pie_charts(df, selected_columns):
    for column in selected_columns:
        plt.figure(figsize=(8, 8))
        df[column].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title(f'Pie Chart of {column}')
        plt.show()

# Function to create line charts for selected columns
def create_line_charts(df, selected_columns):
    for i in range(len(selected_columns)):
        for j in range(i + 1, len(selected_columns)):
            plt.figure(figsize=(10, 6))
            sns.lineplot(x=selected_columns[i], y=selected_columns[j], data=df)
            plt.title(f'Line Chart of {selected_columns[i]} vs {selected_columns[j]}')
            plt.xlabel(selected_columns[i])
            plt.ylabel(selected_columns[j])
            plt.show()

# Function to create box plots for selected columns
def create_box_plots(df, selected_columns):
    for column in selected_columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[column])
        plt.title(f'Box Plot of {column}')
        plt.xlabel(column)
        plt.show()

# Get user input for selected columns
selected_columns = input("Enter column names separated by commas (e.g., column1, column2): ").split(',')

# Create visualizations with selected columns
create_bar_charts(df, selected_columns)
create_scatter_plots(df, selected_columns)
create_histograms(df, selected_columns)
create_pie_charts(df, selected_columns)
create_line_charts(df, selected_columns)
create_box_plots(df, selected_columns)
