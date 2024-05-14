
from flask import Flask, make_response, render_template, send_from_directory, jsonify, request, redirect
import datetime
import simplejson
import config
import json

import re

import adif
import yaarl

from functions import json_response, sanitise_string


def dummy(_message = "not yet implemented"):
    '''
    Returns a dummy 200 response
    '''
    print ("*** Ran Dummy API Function ***")
    return json_response(tag="ok", value=_message, status=200)



def schema_get():
    '''
    Low priority - documentation
    '''
    return dummy()


def convert_get():
    '''
    Handle incoming  GET for conversion
    '''

    _arguments = ["from","to","data"]
    
    _query_string = ""
    _data_dict = {}

    # If we have URL parameters, process them
    if (request.args):

         # Ensure mandatory fields are present
        for _val in _arguments:
            if not _val in request.args:
                return json_response(tag="error",value=f"parameter '{_val}' is missing value.", status=400)

    if (len(request.args['data']) > 0):



        # Convert From
        if request.args['from'] == "adif":
            print (f"{config.colours.OKCYAN}From: ADIF{config.colours.ENDC}") 
            _data_dict = adif.adif_to_dict (request.args['data'])

        elif request.args['from'] == "csv":
            print (f"{config.colours.OKCYAN}From: CSV{config.colours.ENDC}") 
            _data_dict = csv.csv_to_dict (request.args['data'])


        # Convert To
        _result = ""

        if request.args['to'] == "adif":
            print (f"{config.colours.OKCYAN}To: ADIF{config.colours.ENDC}") 
            _result = adif.dict_to_adif (_data_dict)
        
        elif request.args['to'] == "json":
            print (f"{config.colours.OKCYAN}To: JSON{config.colours.ENDC}") 
            _result = json.dumps(_data_dict)

        elif request.args['to'] == "yaarl":
            print (f"{config.colours.OKCYAN}To: Yaarl{config.colours.ENDC}")
            print (_data_dict)
            _result = json.dumps(adif.adif_to_yaarl(_data_dict))

        print (f"Returning: {config.colours.OKCYAN}{_result}{config.colours.ENDC}") 
        return _result

    return dummy()


def convert_post():
    '''
    Handle incoming POST data for conversion
    '''

    _arguments = ["from","to"]

    _query_string = ""

    # If we have URL parameters, process them
    if (request.args):

        print (f"*** {request.args} ***")

   # Check POST data type
    if "application/json" in request.content_type:
        if request.json:
            _new_data = request.json
    elif "application/x-www-form-urlencoded" in request.content_type:
        if request.form:
            _new_data = request.form

    if (len(_new_data) == 0):
        print ("*** Zero Length Data ***")
        return json_response(tag="error", value="send application/json -or- application/x-www-form-urlencoded body", status=400)
    
    # Ensure mandatory fields are present
    
    if not _val in _new_data:
           return json_response(tag="error",value=f"you must supply a value for {_val}", status=400)

    for _val in config.LOGBOOKFIELDS:
        if _val in _new_data:
            _new_entry[_val] = _new_data[_val]
        else:
            _new_entry[_val] = ""

    return dummy()


