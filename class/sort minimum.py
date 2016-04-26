def main():
    A=[5,7,15,1,8]
    i = 0
    min = A[0]
    while i > len(A) -1:
        i = i +1
        if A[i] < min:
            min = A[i]
    print ("The minimum positive integer is" , min)

main()
