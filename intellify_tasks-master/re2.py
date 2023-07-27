import re
fp = open('file.txt')
for line in fp:
    line = line.rstrip()
    x = re.findall('[A-Za-z0-9]+@[A-Za-z0-9]+.com', line)
    if len(x)>0:
        print(x)