import json
import pickle


_locations = None
_array_columns = None
_model = None


def get_approx_price(loc, sqft, bedrooms, bath):
    pass


def get_locations():
    return _locations


def load_artifacts():
    print("loading artifacts information...")
    global _array_columns
    global _locations

    with open("./artifacts/array_columns.json", "r") as file:
        _data_columns = json.load(file)["array_columns"]
        _locations = _data_columns[3:]

    with open("./artifacts/bengaluru_house_price_model.pickle", "rb") as file:
         _model = pickle.load(file)

    print("Loadinng information completed")




if __name__ =="__main__":
    load_artifacts()
    print(get_locations())