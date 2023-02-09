import json
import pickle
import numpy as np


_locations = None
_array_columns = None
_model = None


def get_approx_price(loc, sft, bedrooms, bath):

    try:
        location_index = _array_columns.index(loc.lower())
    except:
        location_index = -1

    x = np.zeros(len(_array_columns))
    x[0] = sft
    x[1] = bath
    x[2] = bedrooms
    if location_index >= 0:
        x[location_index] = 1
    return round(_model.predict([x])[0], 3)


def get_locations():
    return _locations


def load_artifacts():
    print("loading artifacts information...")
    global _array_columns
    global _locations
    global _model

    with open("./artifacts/array_columns.json", "r") as file:
        _array_columns = json.load(file)["array_columns"]
        _locations = _array_columns[3:]

    with open("./artifacts/bengaluru_house_price_model.pickle", "rb") as file:
         _model = pickle.load(file)

    print("Information loading completed")




if __name__ =="__main__":
    load_artifacts()

    # print("House price: ", get_approx_price("Indira Nagar", 1000, 2, 3))