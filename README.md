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
        # This prints the object "cool" to the logger
        output_to_logger(cool)






MORE COMPLICATED STUFF
======================
If you want to do more complicated stuff with this library, go for it! Here
are some guided suggestions


Local Installation
------------------
If you'd like to hack on this library, feel free to! Here are steps to download
and use this library locally:

Create a new python virtual environment

    virtualenv outlib

Go into the new folder created

    cd outlib

Activate your Environment

    source bin/activate

Create a source folder

    mkdir src

Go into the src folder

    cd src

Git clone the repository

    git clone https://github.com/rhintz42/outlib.git

Go into the new folder

    cd outlib

Install all the dependencies and create the egg-file

    python setup.py develop

Install all the test dependencies

    pip install -r test-requirements.txt

Everything should be installed for this project, but now you need to install
this library in your project. Goto the virtual environment of the project you
want to use this library in and activate that environment. Then, go back to
the outlib folder and type this command

    python setup.py develop

This will install outlib in the site-packages folder in that python
environment, so you can now change code in your outlib directory, and it will
affect that project!


How to Run The Tests
--------------------
If you hack on this locally (Which you definitely should!), you should run and
add tests! To run the tests, first install the necessary dependencies (If you
haven't done so already):

    pip install -r test-requirements.txt

After that, just run this command and your tests should run

    py.test


How to Add Tests
----------------
To add tests, just go into the correct folder and add tests!

To add Unit Tests, goto this folder:

    oulib/tests/unit/

If you want to add a Unit Test to a library, goto this folder:

    outlib/tests/unit/lib

Try to follow the naming convention of

    test_<file_name_of_thing_testing>.py

And try to look at a few tests to see the conventions used for tests


How to Make This Library a Dependency for your Python Project
-------------------------------------------------------------
If you have a standard python project that has a setup.py file, it's easy to
make outlib be one of its dependencies. Just follow these steps:

First, add a new array "github_dependencies" above the "setup" method, and
add 'git+git://github.com/rhintz42/outlib.git#egg=outlib' to the array

    github_dependencies = [
        'git+git://github.com/rhintz42/outlib.git#egg=outlib'
    ]

Next, add the library to your 'requires' array

    requires = [
        # The ... signifies all the other packages you require
        ...,
        'outlib'
    ]

Last, add the kwarg 'dependency_links=github_dependcies,' to your setup method

    setup(name='<your_project>',
          ...,
          dependency_links=github_dependencies,
          ...,
          )


Example setup.py from https://github.com/rhintz42/proflib.git:

    import os

    from setuptools import setup, find_packages

    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, 'README.txt')) as f:
        README = f.read()
    with open(os.path.join(here, 'CHANGES.txt')) as f:
        CHANGES = f.read()

    requires = [
        'pyramid',
        'pyramid_chameleon',
        'pyramid_debugtoolbar',
        'waitress',
        'outlib'
        ]

    github_dependencies = [
        'git+git://github.com/rhintz42/outlib.git#egg=outlib'
    ]

    setup(name='proflib',
          version='1.0.1',
          description='proflib',
          long_description=README + '\n\n' + CHANGES,
          classifiers=[
            "Programming Language :: Python",
            "Framework :: Pyramid",
            "Topic :: Internet :: WWW/HTTP",
            "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
            ],
          author='',
          author_email='',
          url='',
          keywords='web pyramid pylons',
          packages=find_packages(),
          include_package_data=True,
          zip_safe=False,
          install_requires=requires,
          dependency_links=github_dependencies,
          tests_require=requires,
          test_suite="proflib",
          entry_points="""\
          [paste.app_factory]
          main = proflib:main
          """,
          )
