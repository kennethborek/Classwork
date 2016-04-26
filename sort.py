def main():
    A=[4,7,3,9,8]
    print ("Before sort: " , A)
        for j in range(len(A)):
        print (A)
             i=0
             for k in range (len(A)-1):
                 if A[i] > A [i+1]:
                     temp=A[i]
                     A[i]=A[i+1]
                     A[i+1] = temp
             i=i+1
    print ("After sort: " , A)

main()