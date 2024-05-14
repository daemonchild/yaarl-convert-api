import yaarl
import config

def adif_to_dict (_data):
    _new_dict = {}
    for _token in _data.split("<"):
        if (len(_token) > 0):
            _chunk = _token.split(">")     
            _fragment = _chunk[0].split(":")
            _key = _fragment[0]          
            if (len(_fragment) > 1):
                _length = _chunk[0].split(":")[1]
            else:
                _length = len(_key)            
            _value = _chunk[1].replace(" ","")
            if (_key != "eor"):
                _new_dict[_key] = _value
    return (_new_dict)


def dict_to_adif (_data):
    _new_string = ""
    for _key in _data.keys():
        _value =_data[_key]
        _length = len(_value)
        _new_tag = f"<{_key}:{_length}>{_value} "
        _new_string += _new_tag
    return _new_string


def adif_to_yaarl (_data):

    print (f"{config.colours.OKGREEN}Converting to Yaarl Format{config.colours.ENDC}") 

    _new_dict = {}
    for _key in _data.keys():

        if _key in yaarl.ADIF_YAARL_MAP.keys():
            _new_key = yaarl.ADIF_YAARL_MAP[_key]
            _value =_data[_key]
            _new_dict[_new_key]=_value

            if _new_key == "log_date":
                print ("!!! Log format is wrong!")

    return _new_dict

def yaarl_to_adif (_data):

    print (f"{config.colours.OKGREEN}Converting to ADIF Format{config.colours.ENDC}") 

    _new_dict = {}
    for _key in _data.keys():

        if _key in yaarl.YAARL_ADIF_MAP.keys():
            _new_key = yaarl.YAARL_ADIF_MAP[_key]
            _value =_data[_key]
            _new_dict[_new_key]=_value

    return _new_dict