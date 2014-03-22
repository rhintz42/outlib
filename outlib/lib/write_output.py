import os
import json

"""
* Be able to have encapsulated in pattern
* Add objects folder can store objects and such
"""
def dict_to_output_list(output):
    output_lines = json.dumps(output, indent=4, sort_keys=True).splitlines()
    return output_lines

def str_to_output_list(output):
    output_lines = output.splitlines()
    return output_lines

def write_output(file_path, output, append=False):
    write_type = 'a' if append else 'w'
    
    if type(output) is str:
        output_lines = str_to_output_list(output)
    if type(output) is dict:
        output_lines = dict_to_output_list(output)
    
    f = open(file_path, write_type)

    for l in output_lines:
        f.write(l+'\n')

    f.close()
