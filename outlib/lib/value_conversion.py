import os
import json
import logging
from outlib.lib.format_vals import format_value

"""
Value Conversion Converts values from regular strings to special formats
"""

def value_to_json(formatted_output, indent=4, sort_keys=True):
    return json.dumps(formatted_output, indent=indent, sort_keys=sort_keys)

def value_to_json_pretty(formatted_output, indent=4, sort_keys=True):
    return json.dumps(formatted_output, indent=indent, sort_keys=sort_keys)

def value_to_output_list(val):
    output_list = []

    formatted_output = format_value(val)

    output_list = value_to_json(formatted_output).splitlines()

    return output_list

def value_to_logger_output(val):
    formatted_output = """
\n========================================================================\n
%s 
\n========================================================================\n
""" % (value_to_json_pretty(format_value(val)))
    return formatted_output
