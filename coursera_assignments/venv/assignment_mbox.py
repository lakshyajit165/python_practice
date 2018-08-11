fname = input("Enter file name: ")
fh = open(fname)
A = []
tot = 0
for line in fh:
    if(line.startswith("X-DSPAM-Confidence:")):
        A.append(float(line.strip().split(':')[1]))

for i in A:
    tot+=i
print("Average spam confidence: "+str(tot/len(A)))