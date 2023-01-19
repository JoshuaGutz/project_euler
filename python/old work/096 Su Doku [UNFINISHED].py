# 96 Su Doku

file_name = "sudoku.txt"
file_handler = open(file_name)

problem = []
line_count = 0
line_start = 0
line_finish = 11
for line in file_handler:
    line_count += 1
    if line_count == 11:
        break
    if line[:4] == "Grid": continue
    line = line.rstrip()
    print line
