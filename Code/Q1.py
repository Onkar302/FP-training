#1. Write an algorithm to reverse a character array. Method signature: public char [] reverse 
#(char [] input).
#Note: 
#1.It is not allowed to use any inbuilt language function
#2. it is not allowed to use any temporary array
#3. Basically it should be an in place reversal 


def revCharArr(arr):
    i = 0; j = len(arr)-1
    while(i <= j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1; j-=1
    print(arr)

revCharArr(['o', 'n', 'k', 'a', 'r'])
    
