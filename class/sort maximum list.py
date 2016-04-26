def main():
    A = [5, 7, 15, 1, 8]
    print(A)
    i = 0
    max = A[0]
    print(i, " ", max)
    while i < len(A) - 1:
        i = i + 1
        if A[i] > max:
            max = A[i]
        print(i, " ", max)
    print("The maximum positive integer is", max)


main()
