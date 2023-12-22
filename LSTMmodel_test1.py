# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 10:19:18 2023

@author: Danille
"""



import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, RepeatVector, Dense, TimeDistributed
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Load data from Excel sheet (assuming the data is in the first sheet)
excel_path = 'C:/Users/Danille/Desktop/Gebied_07/CSV/TBL_Sporen.xlsx'
df = pd.read_excel(excel_path)

# Identify numerical columns for visualization
numerical_columns = df.select_dtypes(include=[np.number]).columns.tolist()

# Check if there are numerical columns
if not numerical_columns:
    print("No numerical columns found in the Excel sheet. Please ensure your data contains numerical values.")
else:
    # Extract the numerical columns from the DataFrame
    selected_data = df[numerical_columns].values

    # Normalize the data using Min-Max scaling
    scaler = MinMaxScaler()
    selected_data_normalized = scaler.fit_transform(selected_data)

    # Reshape the data for LSTM input (assuming each row is a sequence)
    input_sequences = selected_data_normalized.reshape((1, selected_data.shape[0], selected_data.shape[1]))

    # Define the model
    model = Sequential()

    # Encoder
    model.add(LSTM(units=256, input_shape=(input_sequences.shape[1], input_sequences.shape[2])))

    # Repeat the encoded vector to match the target sequence length
    model.add(RepeatVector(input_sequences.shape[1]))

    # Decoder
    model.add(LSTM(units=256, return_sequences=True))
    model.add(TimeDistributed(Dense(units=input_sequences.shape[2], activation='linear')))  # Using linear activation for regression

    # Compile the model
    model.compile(optimizer='adam', loss='mean_squared_error')  # Adjust loss function for regression

    # Print a summary of the model architecture
    model.summary()

    # Define the number of training epochs and batch size
    epochs = 10  # Replace with your desired number of epochs
    batch_size = 32  # Replace with your desired batch size

    # Train the model
    model.fit(input_sequences, input_sequences, epochs=epochs, batch_size=batch_size)  # Using input data as target for simplicity

    # Use the trained model to make predictions
    predictions = model.predict(input_sequences)

    # Visualize the data and predictions
    for i, header in enumerate(numerical_columns):
        plt.plot(selected_data[:, i], label=f'Input {header}')
        plt.plot(predictions[0, :, i], label=f'Predicted {header}')
        plt.legend()
        plt.xlabel('Time Steps')
        plt.ylabel('Values')
        plt.title(f'Visualization of {header}')
        plt.show()
