import pickle
import json
import numpy as np

__data_columns = ['area', 'bedrooms', 'bathrooms']
__model = None

def get_estimated_price(area, bedrooms, bathrooms):
    x = np.zeros(len(__data_columns))
    x[0] = area
    x[1] = bedrooms
    x[2] = bathrooms

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns

    with open("C:/Users/HP/Downloads/legnd/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']

    global __model
    if __model is None:
        with open('C:/Users/HP/Downloads/legnd/linear_regression_model.pkl', 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts...done")


def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()

    estimated_price = get_estimated_price(area=1000, bedrooms=3, bathrooms=3)
    print(estimated_price)
    #print(get_estimated_price(1000, 2, 2))
    #print(get_estimated_price(1000, 2, 2))  # other location
    #print(get_estimated_price(1000, 2, 2))  # other location