def main():
    A=[5,7,15,1,8]
    i = 0
    max = A[0]
    while i < len(A) -1:
        i = i +1
        if A[i] > max:
            max = A[i]
    print ("The maximum positive integer is" , max)

main()