FILE_NAME = "./dictionary.txt"

f = open(FILE_NAME, "r")
for line in f:
    line = line.strip()
    line = line.lower()
    if (line[0] == line[-1] and line[0] == 'o'):
        print(line)