def Nge(arr):
    for i in range(0 , len(arr) , 1):
        next = -1
        for j in range(i+1 , len(arr) , 1):
            if arr[i] < arr[j]:
                next = arr[j]
                #print(next)
                break

        print(str(arr[i]) + ' -- ' + str(next))

arr = [2,5,78,89,3,7,2,100]
Nge(arr)

