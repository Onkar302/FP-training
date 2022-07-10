#2. Find number of occurrences of each number from the array
#Every number is in the range [0….100].
#Public void numberOfOccurences (int [] input){
#//write logic here
#}
#Note: expecting O(n) solution which means no sorting or nested loops allowed

def countOccurrences(arr):
    i = 0; counter = [0]*101
    while(i < len(arr)):
        counter[arr[i]] += 1
        i += 1

    print(counter)

countOccurrences([1, 3, 11, 17, 26, 100, 20, 40, 60, 80, 97, 97, 17, 35, 33, 29, 88])
