import re
fp = open('file.txt')
for line in fp:
    line = line.rstrip()
    if re.search('[A-Za-z0-9]+@[A-Za-z0-9]+.com', line):
        print(line)