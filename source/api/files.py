'''

File:       files.py
Purpose:    File handling handling functions

'''

# Import Python Libraries
import json
import os
from flask import send_from_directory

def file_load_json(_file_name):

    _load_data = {}

    try:
        with open(_file_name, 'r') as _f:
            _load_data = json.load(_f)

        return _load_data

    except IOError:
        print(f"I/O error loading {_file_name}")
        exit(1)


# Not linked, not used currently below here...


def api_load_csv():

    global issues

    inputfile = 'saved.csv'

    columns = issuefields

    # Empty the database
    issues = []

    try:
        with open(inputfile, 'r') as csvfile:
            reader = csv.DictReader(csvfile)

            for newissue in reader:
                # fix up for float and int values in the data to allow sorting
                cvss = CVSS3(newissue['cvssvector'])

                severities = cvss.severities()
                scores = cvss.scores()

                newissue['severity'] = severities[0]

                # We prefer Info to None :)
                if severities[0] == "None":
                    newissue['severity'] = "Info"

                newissue['cvssscore'] = float(scores[0])

                issues.append (newissue)

            sort_issues_cvss()


    except IOError:
        print("I/O error")

    return make_response(jsonify({'success': 'Loaded ' + str(len(issues)) + ' issues'}), 200)