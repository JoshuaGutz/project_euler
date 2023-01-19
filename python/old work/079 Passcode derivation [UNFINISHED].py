# 79 Passcode derivation

def instructions():
    # A common security method used for online banking is to ask the 
    # user for three random characters from a passcode. For example, if 
    # the passcode was 531278, they may ask for the 2nd, 3rd, and 5th 
    # characters; the expected reply would be: 317.

    # The text file, keylog.txt, contains 50 successful login attempts.

    # Given that the three characters are always asked for in order, 
    # analyse the file so as to determine the shortest possible secret 
    # passcode of unknown length.
    pass
pass

def open_file(): # outputs sorted keylog list of 33 unique keys
    global keylog
    keylog = []
    file_handler = open("keylog.txt")
    for line in file_handler:
        line = int(line.rstrip())
        if line in keylog : continue
        keylog.append(line)
    pass
    keylog.sort()
open_file()
print keylog

