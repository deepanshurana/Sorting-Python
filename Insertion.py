def insertionsort(A):

    for i in range (1, len(A)):
        temp = A[i]
        k = i

        while k>0 and temp > A[k-1]:
            A[k] = A[k-1]
            k -= 1
            A[k] = temp

A = [23,5,21,34,65,64,6,234,686,23]
insertionsort(A)
print(A)


