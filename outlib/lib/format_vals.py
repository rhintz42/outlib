import json

"""
This module is meant to help programmers format their values into json
    serializable values
"""

"""
* Be able to have encapsulated in pattern
* Add objects folder can store objects and such and write function to dumps those
"""
def _format_dict(dict_input):
    formatted_output_dict = {}

    for key,val in dict_input.items():
        formatted_output_dict[key] = format_value(val)

    return formatted_output_dict

def _format_list(list_input):
    """
    Make sure all of the types of objects inside the list are able to output
        to JSON.
    * If an object is unable to output to JSON as-is, try to make it into a
        format that can be
    * If all fails, log exception
    """
    formatted_list = []

    for val in list_input:
        formatted_list.append(format_value(val))

    return formatted_list
        
def _format_object(obj_input):
    formatted_output_dict = _format_dict(obj_input.__dict__)
    return formatted_output_dict

def _format_row_proxy(row_proxy_input):
    output_dict = {}
    for key in row_proxy_input.keys():
        output_dict[key] = row_proxy_input[key]

    formatted_output_dict = _format_dict(output_dict)

    return formatted_output_dict

def format_value(val):
    if type(val) is str or type(val) is int or type(val) is long:
        return val
    elif type(val) is dict:
        return _format_dict(val)
    elif type(val) is list:
        return _format_list(val)
    elif type(val).__name__ is 'RowProxy':
        return _format_row_proxy(val)
    else:
        return _format_object(val)

def format_for_logger(val):
    return val
