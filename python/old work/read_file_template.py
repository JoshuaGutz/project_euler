file_name = raw_input("Enter file name: ")
if len(file_name) == 0:
    file_name = "FILE_NAME_HERE.txt"
try:
    file_handler = open(file_name)
except:
    print "File cannot be opened:", file_name
    exit()
for line in file_handler:
    line = line.rstrip()
    print line
file_name.close()