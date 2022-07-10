#7. Given two sorted arrays in ascending order , write a function which takes both as input 
#and returns an array of common elements .
# A = [1,3,4,6,7,9]
# B=[1,2,4,5,9,10]
# OutputArray:[1,,4,9]
#Note: Solution should be in O(n)

def intersection(arr1, arr2):
    i = 0
    j = 0
    result = []
    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] == arr2[j]):
            result.append(arr1[i])
            i += 1
            j += 1 
        elif(arr1[i] > arr2[j]):
            j += 1
        else:
            i += 1
    print(result)

intersection([1,3,4,6,7,9],[1,2,4,5,9,10])
intersection([22, 35, 38, 46, 54], [27, 38, 49, 50])
