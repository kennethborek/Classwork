#The following program result should be a sorted list focusing on the minimum value.
def main():
    A = [5, 7, 15, 1, 8]
    print(A)
    i = 0
    min= A[0]
    print(i, " ", min)
    while i > len(A) - 1:
        i = i + 1
        if A[i] < min:
            min = A[i]
        print(i, " ", min)
    print("The minimum positive integer is", min)


main()
