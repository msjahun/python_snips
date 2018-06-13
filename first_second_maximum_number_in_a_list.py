if __name__ == '__main__':
    n = int(input())
    arr = list( map(int, input().split()))
   # print(arr)
    min1 = -100
    min2= -100
    for i in range(n):
       
        
        #print("index and value", end="")
       # print(i, end=" ")
        #print(arr[i])
        
        if(arr[i]==min2):
            continue
        if(arr[i]>=min2):
            min1=min2
            min2=arr[i]
        elif(arr[i]>=min1):
            min1=arr[i]
     
    print( min1)