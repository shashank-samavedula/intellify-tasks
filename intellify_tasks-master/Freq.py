fname=input("Enter file name:")
try:
    fhand=open(fname)
except:
    print("File cannot be opened")
    exit()
d=dict()
for line in fhand:
    for word in line.split():
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1 
#print(d)

listofTuples = sorted(d.items() ,  key=lambda x: x[1])
print(listofTuples[-1])