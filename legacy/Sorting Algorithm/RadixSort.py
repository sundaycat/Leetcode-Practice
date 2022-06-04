# value of A represent its position in C
# value of C represent its position in B
def count_sort(A, k, exp):
    B = [0 for i in range(len(A))] 
    C = [0 for i in range(k)]

    # count the frequency of each elements in A and save them in the coresponding position in B
    for i in range(0, len(A)):
        # calculate the index for A[i] in C array
        index = A[i] // exp % 10
        C[index] += 1

    # accumulated sum of C, indicating where we should put in Aay B
    for i in range(1, k, 1):
        C[i] = C[i - 1] + C[i]

    # build the output array
    for i in range(len(A)-1, -1, -1):
        index = A[i] // exp % 10

        # convert the location to index
        B[C[index] - 1] = A[i]
        C[index] -= 1
    
    # copying the output array to arr[], so that arr now contains sorted numbers
    for i in range(len(A)):
        A[i] = B[i]


def radix_sort(arr):
    # Find the maximum number to know number of digits
    max_num, exp = max(arr), 1

    # Do counting sort for every digit. Note that instead of passing digit number, exp is passed. exp is 10^i
    # where i is current digit number
    while max_num // exp > 0:
        count_sort(arr, 10, exp)
        exp *= 10
    return arr
    
arr = [170, 45, 75, 90, 802, 24, 2, 66, 1000, 20, 1010]
print(radix_sort(arr))