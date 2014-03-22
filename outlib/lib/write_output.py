import os

"""
* Be able to have encapsulated in pattern
"""

def write_output(file_path, output, append=False):
    write_type = 'a' if append else 'w'
    
    f = open(file_path, write_type)
    f.write(output)
    f.close()
