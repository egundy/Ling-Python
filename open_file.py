# script to create a module to open a file quickly
# define a function to open a file

def open_file(filename):
    with open(filename, 'r') as f:
        return f.read()