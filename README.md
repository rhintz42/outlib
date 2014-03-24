outlib
======

This library provides a wrapper for writing output to either a console or a
file. You can give it any type of data, and it will try its best to output it
in a format that makes most sense to you. It attempts to make how it outputs
customizable, so anyone can change how their data is printed out.

This library was made to accompany https://github.com/rhintz42/proflib.git.
Much of the tests have been written using proflib.


Overview
--------
The basic concept is to make it as easy as possible to print in a way that
makes most sense to the user. Whether you want to log the data to the terminal
or to a file, this library tries to make the distinction as easy as possible.


Why We Build It
---------------
The purpose of this is to make it extremely easy to write out information to
the terminal or to a file


Installation
------------
To install OutLib, enter this command in the virtual environment you want to
use the library in
    
    pip install git+git://github.com/rhintz42/outlib.git#egg=outlib


How to Use
----------
Using this library is extremely easy, all you need to do is import the library
to your file and add the function you wish to use with the object you want to 
print

Add this line to the top of the file that has the function you wish to profile:

    from outlib.lib.wout import output_to_logger

Then, add the wrapper right above the function you wish to profile:

    output_to_logger(object_to_print)

Example:

    from outlib.lib.wout import output_to_logger

    def test_function(cool):
        output_to_logger(cool)
