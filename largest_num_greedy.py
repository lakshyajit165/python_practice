A = [3,7,9,5,9,1]
#arrange all the digits of the list in such a way that they form the largest number
largest = []
while(len(A)!=0):
    temp = max(A)
    largest.append(temp)
    A.remove(temp)
for i in largest:
    print(i,end='')