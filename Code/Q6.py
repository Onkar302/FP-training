#6. Write a function that takes in an integer array and returns the item that occurs most 
#often.
#int Most_frequent(inputArray [])
#If n is an input element in the array the possible values for n 1 ≤ n ≤ 100
#Note: Solution should be in O(n)

def Most_frequent(arr):
    i = 0
    freq_dict = {}
    while(i < len(arr)):
        if(arr[i] in freq_dict):
            freq_dict[arr[i]] += 1
        else:
            freq_dict[arr[i]] = 1
        i += 1;

    maxElement = arr[0]
    maxOcc = freq_dict[arr[0]]
    for ele in freq_dict:
        if(freq_dict[ele] > maxOcc):
            maxElement = ele
            maxOcc = freq_dict[ele]

    print("The most frequent element is ", maxElement)

Most_frequent([20, 1, 2, 78, 2, 14])
Most_frequent([32, 4, 16, 72, 3, 3, 87, 4, 4])
        
