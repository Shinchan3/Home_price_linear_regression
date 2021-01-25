import flask
import pickle
import json
import numpy as np
__data_col=None
__columns=None
__model=None
def get_location():
    global __columns
    global __model
    global __data_col
    with open('./things/colums.json','r') as f:
        __data_col=json.load(f)['data_columns']
        __columns = __data_col[4:]

    with open("./things/bangluru_home_price.pickle",'rb') as f:
        __model=pickle.load(f)
        # f.get_predict()
    return __columns
def estimated_price(location,size,bhk,balcony,bath):
    global __model
    try:
        index = __data_col.index(location.lower())
    except:
        index =-1
    x=np.zeros(len(__data_col))
    x[0]=size
    x[1]=bath
    x[2]=balcony
    x[3]=bhk
    if(index>=0):
        x[index]=1

    return __model.predict([x])[0]
if __name__ == "__main__":
    get_location()
    print(estimated_price('1st phase jp nagar',1000,2,2,2))
    print(estimated_price('indira nagar',1000,2,2,2))