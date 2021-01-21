INTRODUCTION
------------
The purpose of this project was to create a BMI calculator for a college project. I had the option of using a GUI or making it a CLI.

I decided to make it as  a command line based project. 

REQUIREMENTS
------------

This module requires the following modules:

* argparse
* datetime
* csv
* os

DESCRIPTION
------------

Although BMI isn't an optimal way to measure someones health, this was a very interesting project to work on. It really allowed me to apply some of the things I learned from this course. It also allowed for me to learn about argparse. Using argparse for this task allowed me to make a simple and user-friendly command line project and I feel it suited the task quite well.

EXECUTING PROGRAM
-----------------

* Open command line
* Move to the directory where the file has been saved
* Enter "python3 bmi_converter.py 'first name' 'surname' 'height in meters' 'weight in kg' " for a standard BMI calculation.
* The use of optional arguments is also possible.
    * The use of '--imperial' at the end of your command will change the system from metric to imperial. The user will enter their height in feet and weight in stone.
    * The use of '-w' at the end of your command will save the users information to a file called 'measurements'

HELP
----

* The use of '-h' at the end of the command will bring up a list of positional arguments and optional arguments that the user should use.

AUTHORS
-------

* Michael Lenahan
