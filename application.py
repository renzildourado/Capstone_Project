import csv
import pickle

import flask, flask.views
import ast
from flask import request
app = flask.Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def hello_world():
    return "The Server works"


@app.route("/predict", methods = ["POST"])
def get_permissions():

    received_json_object = request.get_json()
    permission_list_string = received_json_object["permissionList"]

    #Getting rid of [ and ] in the string [ "A", "B" ]
    permission_list_string = permission_list_string[1:len(permission_list_string)-1]

    #Turning the string into an actual python list
    permission_list = ast.literal_eval(permission_list_string)

    prediction = perform_predict(permission_list)

    # permission_list_stringit g_return = "The Permissions are:\n"
    #
    # for permission in permission_list:
    #     permission_list_string_return += permission
    #     permission_list_string_return += "\n"

    return prediction


def perform_predict(permission_list):
    csv_reader = csv.reader(open("attributes.csv", "r"))
    all_permissions_list = []
    permission_list_dict = set()
    predict_list = []

    for line in csv_reader:
        if len(line)>0 and line[0]!= "MALWARE_DETECTION":
            all_permissions_list.append(line[0])

    for permission in permission_list:
        permission_list_dict.add(permission)

    for permission in all_permissions_list:
        if permission in permission_list_dict:
            predict_list.append(1)
        else:
            predict_list.append(0)

    linear_regression = pickle.load(open("random_forest_model_new.sav", 'rb'))
    prediction = linear_regression.predict([predict_list])

    if prediction[0]==0:
        return "No"
    else:
        return "Yes"

if __name__ == '__main__':
    app.debug = True
    app.run()