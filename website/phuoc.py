# import cv2
from tensorflow import keras
import os
from keras.models import load_model
import numpy as np
import csv

def coverData(flow,pressure):
    file_path = 'data/data.csv'

    array = []
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            array.append(row)
    
    for index in array[-99:]:
        array_index = [float(index[1]),float(index[2])]
        data.append(array_index)
    new_data = [flow,pressure]
    data.append(new_data)
    print (len(data))
    
    # add_values_to_last_row(file_path, flow, pressure)

    return data


def predictions(x_prediction):
    x_prediction = np.array(x_prediction).reshape(1,len(x_prediction),len(x_prediction[1]))
    print(x_prediction.shape)
    loaded_model = load_model('models/best_model.h5')
    y_predictions_scaled = loaded_model.predict(x_prediction)
    y_predictions_scaled = y_predictions_scaled.flatten()
    y_predictions_scaled = float(y_predictions_scaled[0])
    return y_predictions_scaled



def add_values_to_last_row(file_path, flow, pressure):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    last_row = rows[-1]
    last_row[1] = flow 
    last_row[2] = pressure  

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)