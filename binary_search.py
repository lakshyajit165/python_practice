def bin_search(a,l,r,x):

    if(r >= l):
        mid = l + (r-l)//2

        if(a[mid] == x):
<<<<<<< HEAD
            return(mid)
=======
<<<<<<< HEAD
            return(mid)
=======
            return(mid+1)
>>>>>>> 3fd2e0bf3056c187a4af3d5a6e8bb83949d7212a
>>>>>>> ec8b96507fecaa7a6c3b72561e9c555851fe633d
        elif(a[mid] > x):
            return(bin_search(a,l,mid-1,x))
        else:
            return(bin_search(a,mid+1,r,x))
    else:
        return(-1)
A = list(map(int,input().split()))
n = len(A)
x = int(input())
print(bin_search(A,0,n-1,x))