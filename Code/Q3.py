#3. Find first maximum and second maximum number from an integer array
#Note : expecting O(n) solution which means no sorting or nested loops allowed

def maximums(arr):
    max1 = max2 = arr[0]
    i = 1
    while(i < len(arr)):
        if(arr[i] > max1):
            max2 = max1
            max1 = arr[i]
    
        elif(arr[i] < max1 & arr[i] > max2):
            max2 = arr[i]

        i += 1

    print("First Maximum is ", max1, " Second Maximum is ", max2)

maximums([20, 77, 1, 4, 402])
maximums([-20, -99, -1, 24])
            
             
