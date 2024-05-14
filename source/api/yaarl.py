import files
import config


_schema_data = dict(files.file_load_json(config._data_file_path + "schema_yaarl.json"))


YAARL_FIELDS = list(_schema_data['logbook'][0].keys())

YAARL_FIELDS_REQUIRED = []
for field in YAARL_FIELDS:
    if (_schema_data['logbook'][0].get(field) == "mandatory"):
        YAARL_FIELDS_REQUIRED.append(field)

_yaarl_adif_map_json = files.file_load_json(config._data_file_path + "schema_yaarl_adif_map.json")
YAARL_ADIF_MAP = _yaarl_adif_map_json['logbook'][0]

ADIF_YAARL_MAP = inv_map = {v: k for k, v in YAARL_ADIF_MAP.items()}