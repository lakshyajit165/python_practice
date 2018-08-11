fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.strip().split(' ')
    for w in words:
        if(w not in lst):
            lst.append(w)
lst.sort()
print(lst)