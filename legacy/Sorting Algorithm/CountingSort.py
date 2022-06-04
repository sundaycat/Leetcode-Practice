# value of A represent its position in C
# value of C represent its position in B
def count_sort(A, k):
    B = [0 for i in range(len(A))] 
    C = [0 for i in range(k)]

    # count the frequency of each elements in A and save them in the coresponding position in B
    for i in range(0, len(A)):
        C[A[i] - 1] += 1

    # accumulated sum of C, indicating where we should put in Aay B
    for i in range(1, k, 1):
        C[i] = C[i - 1] + C[i]

    # count the
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]-1]-1] = A[i]
        C[A[i]-1] -= 1
    
    return B



B = count_sort([4, 1, 3, 4, 3], 4)
print(B)