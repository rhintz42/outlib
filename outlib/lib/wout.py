import os
import json
import logging
from outlib.lib.format_vals import format_value
from outlib.lib.value_conversion import value_to_json, value_to_output_list, \
                                        value_to_json_pretty, \
                                        value_to_logger_output

"""
WOUT means "Write Output"
* This module allows users to write formatted output to a file or logger
* If you want more control over the output, goto the format_vals module and use
    the "format_value" function
"""
def output_to_file(file_path, input_var, append=False):
    write_type = 'a' if append else 'w'

    output_list = value_to_output_list(input_var)

    f = open(file_path, write_type)

    for l in output_list:
        f.write(l+'\n')

    f.close()

def output_to_logger(input_var, logger_type="info", logger=None):
    formatted_output = value_to_logger_output(input_var)

    logging.info(formatted_output)
