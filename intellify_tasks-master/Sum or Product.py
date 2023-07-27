n = int(input("enter n: "))
sum = 0
product = 1
i = 1
choice = input('Enter choice: ')
if choice == 'sum':
    sum = (n*(n+1))/2
    print('Sum = ',sum)

if choice == 'product':
    while i<n:
        product = product*i
        i = i+1
    print('Product = ',product)