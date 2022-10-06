def readfile(filename):
    with open(filename,'r') as file_in:
        text = file_in.read()
    return text
