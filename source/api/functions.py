from flask import jsonify
import re



def json_response(tag,value,status):

    if len(value) == 0:
        return jsonify({tag: ""}),status
    else:
        return jsonify({tag: value}),status



def sanitise_string (input):

    output = re.sub(r'[^A-Za-z_]', '', input)
    return output