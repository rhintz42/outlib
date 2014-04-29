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
        try:
            d = json.dumps(val)
            formatted_output_dict[key] = val
        except:
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
        try:
            d = json.dumps(val)
            formatted_list.append(val)
        except:
            formatted_list.append(format_value(val))

    return formatted_list
        
def _format_object(obj_input):
    if 'to_dict' not in dir(obj_input):
        if not hasattr(obj_input, '__dict__'):
            # TODO: This is temporary. Should really try to check otherways
            # whether can parse the object or not
            return {}
        if obj_input.__class__.__name__ == 'function':
            return "<function: %s>"%(obj_input.__name__)
        return format(obj_input.__dict__)
        
    return _format_dict(obj_input.to_dict()) 

def _format_row_proxy(row_proxy_input):
    output_dict = {}
    for key in row_proxy_input.keys():
        output_dict[key] = row_proxy_input[key]

    formatted_output_dict = _format_dict(output_dict)

    return formatted_output_dict

# The user should be able to define classes they want formatted in a certain way
#   Example: Question class
# The user should be able to allow user to specfy the name of the function to
#   execute to make function into a dictionary
#   Example: to_dict
#   * http://stackoverflow.com/questions/7936572/python-call-a-function-from-string-name
def format_value(val):
    if type(val) is str or \
       type(val) is int or \
       type(val) is long or \
       type(val) is float or \
       val is None:
        return val
    elif type(val) is dict:
        return _format_dict(val)
    elif type(val) is list:
        return _format_list(val)
    # ADD TEST FOR TUPLES
    elif type(val) is tuple:
        return _format_list(val)
    elif type(val).__name__ is 'RowProxy':
        return _format_row_proxy(val)
    else:
        return _format_object(val)
