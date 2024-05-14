#
#                             _ 
#      _   _  __ _  __ _ _ __| |
#     | | | |/ _` |/ _` | "__| |
#     | |_| | (_| | (_| | |  | |
#      \__, |\__,_|\__,_|_|  |_|
#      |___/                    
#  Yet Another Amateur Radio Logger
#        Log Conversion API
# 
#       MW0KKR - Tom Rowan
#

#   app.py
#   - Main Flask App Functions


# ---- Import Libraries ---- 

from flask import Flask, make_response, jsonify, request
import api
import config
from functions import json_response as json_response


# ---- GLOBAL Variables ---- 

APPNAME = "yaarl-conversion-api"
VERSION = "v0.1"

# ---- Flask App Code ----

app = Flask(__name__)

# ---- Global App Functions ---- 

@app.errorhandler(404)
def this_404(error):
    return json_response(tag="error", value="not found", status=404)

@app.errorhandler(503)
def this_503(error):
    return json_response(tag="error", value="database unavailable", status=503)

@app.errorhandler(500)
def this_500(error):
    return json_response(tag="error", value="server error", status=500)
    


# ---- Add API Routes - Use Method as Verb (Get, Delete etc) ----

# -- API Documentation --
# Return internal schemas
app.add_url_rule(rule="/convert/schema", view_func=api.schema_get, methods=["GET"])

# -- Conversion--
app.add_url_rule(rule="/convert/", view_func=api.convert_get, methods=["GET"])
app.add_url_rule(rule="/convert/", view_func=api.convert_post, methods=["POST"])


# ---- Main Application Loop ----
if __name__ == "__main__":

    app.run(debug=True, host="0.0.0.0", port=7374)