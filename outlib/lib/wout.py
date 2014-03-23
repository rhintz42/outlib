import os
import json
import logging
from outlib.lib.format_vals import format_value, format_for_logger

"""
WOUT means "Write Output"
* This module allows users to write formatted output to a file or logger
* If you want more control over the output, goto the format_vals module and use
    the "format_value" function
"""

def value_to_json(formatted_output, indent=4, sort_keys=True):
    return json.dumps(formatted_output, indent=indent, sort_keys=sort_keys)

def value_to_output_list(val):
    output_list = []

    formatted_output = format_value(val)

    output_list = value_to_json(formatted_output).splitlines()

    return output_list

def output_to_file(file_path, input_var, append=False):
    write_type = 'a' if append else 'w'

    output_list = value_to_output_list(input_var)

    f = open(file_path, write_type)

    for l in output_list:
        f.write(l+'\n')

    f.close()

def output_to_logger(input_var, logger_type="info", logger=None):
    output = format_for_logger('\n\n' + input_var + '\n\n')
    logging.info(output)
