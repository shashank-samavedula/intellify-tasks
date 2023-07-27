import math 

def primeFactors(n): 
    
     while n % 2 == 0: 
        print(2,end=" ") 
        n = int(n / 2)
        
     for i in range(3,int(math.sqrt(n))+1,2): 
        
        while n % i== 0: 
            print(i,end=" ") 
            n = int(n / i)
            
     if n > 2: 
        print(n) 
        
n = int(input("Enter value of n: "))
primeFactors(n) 


