'''

File:       config.py
Purpose:    App Config and Data Structures

'''

# Import Python Libraries
import os

# Import DIAF Libraries
import files

# ---- Versions ----

VERSION = "v0.1"
AUTHOR  = "daemonchild"


# ---- Colour Definitions ----

class colours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# -- Data Files --

_app_path = os.path.dirname(os.path.realpath(__file__ ))
_data_file_path = _app_path + '/data_files/'

_config = dict(files.file_load_json(_data_file_path + "config.json")['app_config'])

READ_FORMATS = [
    'adif',
    'yaarl',
    'csv'
]

WRITE_FORMATS = [
    'adif',
    'yaarl',
    'csv',
    'webhook',
    'mysql'
]