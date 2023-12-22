# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:33:09 2023

@author: Danille
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from Excel sheet
excel_path = 'C:/Users/Danille/Desktop/Gebied_07/CSV/TBL_Sporen.xlsx'
df = pd.read_excel(excel_path)

# Function to create bar charts for all combinations of two columns
def create_bar_charts(df):
    columns = df.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            plt.figure(figsize=(10, 6))
            sns.countplot(x=columns[i], hue=columns[j], data=df)
            plt.title(f'Bar Chart of {columns[i]} vs {columns[j]}')
            plt.xlabel(columns[i])
            plt.ylabel('Count')
            plt.legend(title=columns[j])
            plt.show()

# Function to create scatter plots for all combinations of two columns
def create_scatter_plots(df):
    columns = df.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            plt.figure(figsize=(10, 6))
            sns.scatterplot(x=columns[i], y=columns[j], data=df)
            plt.title(f'Scatter Plot of {columns[i]} vs {columns[j]}')
            plt.xlabel(columns[i])
            plt.ylabel(columns[j])
            plt.show()

# Function to create histograms for all columns
def create_histograms(df):
    columns = df.columns

    for column in columns:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column], bins=20, kde=True)
        plt.title(f'Histogram of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

# Function to create pie charts for all columns
def create_pie_charts(df):
    columns = df.columns

    for column in columns:
        plt.figure(figsize=(8, 8))
        df[column].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title(f'Pie Chart of {column}')
        plt.show()

# Function to create line charts for all combinations of two columns
def create_line_charts(df):
    columns = df.columns

    for i in range(len(columns)):
        for j in range(i + 1, len(columns)):
            plt.figure(figsize=(10, 6))
            sns.lineplot(x=columns[i], y=columns[j], data=df)
            plt.title(f'Line Chart of {columns[i]} vs {columns[j]}')
            plt.xlabel(columns[i])
            plt.ylabel(columns[j])
            plt.show()

# Function to create box plots for all columns
def create_box_plots(df):
    columns = df.columns

    for column in columns:
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=df[column])
        plt.title(f'Box Plot of {column}')
        plt.xlabel(column)
        plt.show()

# Create visualizations
create_bar_charts(df)
create_scatter_plots(df)
create_histograms(df)
create_pie_charts(df)
create_line_charts(df)
create_box_plots(df)
