n = int(input('Enter n: '))
sum =0
i =1
while i<n:
    if i%3==0 or i%5==0:
        sum=sum+i
    i=i+1
print('Sum = ',sum)