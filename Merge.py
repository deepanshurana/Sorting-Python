def mergesort(A):
    if len (A) > 1:
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        mergesort(lefthalf)
        mergesort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                A[k] = lefthalf[i]
                i = i+1

            else:
                A[k] = righthalf[j]
                j = j+1

            k = k+1


        while i < len(lefthalf):
            A[k] = lefthalf[i]
            i = i+1
            k = k+1


        while j < len(righthalf):
            A[k] = righthalf[j]
            j = j+1
            k = k+1

A = [23,42,12,54,76,23,78,23,8,75]
mergesort(A)
print(A)



