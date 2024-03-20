import cv2
from keras.models import load_model
import numpy as np
import csv
import os
from .. import models
from ..models import session
from datetime import datetime
from sqlalchemy import desc, asc


def coverData(flow_new, pressure_new):
    result = (
        session.query(models.Data).order_by(
            desc('date')).limit(198).all()
    )
    result_array = []
    for data in result:
        flow = float(data.flow)
        pressure = float(data.pressure)
        array = [flow, pressure]
        result_array.append(array)
    result_array.append([flow_new, pressure_new])
    data = np.array(result_array)
    print(len(result))
    print(data.shape)
    return data


def predictions(x_prediction):
    x_prediction = np.array(x_prediction).reshape(
        1, len(x_prediction), len(x_prediction[1]))

    loaded_model = load_model(
        'backend/models_AI/best_model_24.h5')
    y_predictions_scaled = loaded_model.predict(x_prediction)
    print(y_predictions_scaled)
    y_predictions_scaled = y_predictions_scaled.flatten().tolist()

    return {"array": y_predictions_scaled}


def add_data(request):
    request.date = datetime.now()
    session_history = models.Data(
        date=request.date, pressure=request.pressure, flow=request.flow)

    session.add(session_history)
    # session.commit()
    # session.close()
    try:
        session.commit()
    except Exception as ex:
        session.rollback()
        raise ex
    finally:
        if session:
            session.close()


def add_history(request):
    request.date = datetime.now()
    print(request.location)
    with open('/Users/admin/Downloads/hinh-nen-full-hd-cho-laptop-1.jpg', 'rb') as file:
        request.image = file.read()
    session_history = models.History(
        date=request.date, location=request.location, image=request.image)

    session.add(session_history)
    # session.commit()
    # session.close()
    try:
        session.commit()
    except Exception as ex:
        session.rollback()
        raise ex
    finally:
        if session:
            session.close()


def get_data():

    result = (
        session.query(models.Data).order_by(
            asc('date')).all()
    )
    # result_array = []
    # for data in result:
    #     flow = float(data.flow)
    #     pressure = float(data.pressure)
    #     print(data.date)
    #     array = [flow, pressure]
    #     result_array.append(array)
    # data = np.array(result_array)
    print(len(result))
    session.close()
    return len(result)


def get_history(date_in):

    result = (
        session.query(models.History).order_by(
            asc('date')).filter(models.History.date.like(f'%{date_in}%')).first()
    )
    session.close()

    image_data = result.image

    pre_img = np.frombuffer(image_data, np.uint16)
    print(pre_img)
    image = cv2.imdecode(pre_img, cv2.IMREAD_COLOR)
    original_height, original_width = image.shape[:2]
    new_width = 1920
    new_height = 1080
    image = cv2.resize(image, (new_width, new_height))
    cv2.imwrite('new_image.jpg', image)

    return {
        "text": image.shape}
