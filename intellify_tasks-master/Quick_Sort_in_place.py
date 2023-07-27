def partition(arr,low,high): 
    i = low-1          
    pivot = arr[high]      
  
    for j in range(low , high):  
        if   arr[j] < pivot: 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return i+1 
  
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
 
arr = [2,3,4,5,1,6]
print("List before sorting",arr)
quickSort(arr,0,len(arr)-1)
print("List after sorting",arr)
 
