def lcs(X, Y): 
    L = [[0 for x in range(len(Y)+1)] for x in range(len(X)+1)] 

    for i in range(len(X)+1): 
        for j in range(len(Y)+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
 
    index = L[len(X)][len(Y)] 

    lcs = [""] * (index+1) 
    lcs[index] = "" 

    i = len(X) 
    j = len(Y)
    while i > 0 and j > 0: 

        if X[i-1] == Y[j-1]: 
            lcs[index-1] = X[i-1] 
            i-=1
            j-=1
            index-=1

        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1

    print("LCS: ","".join(lcs))
    print("Length of LCS : ", L[len(X)][len(Y)])
    
X = input("Enter String 1 : ")
Y = input("Enter String 2 : ")
lcs(X, Y) 

