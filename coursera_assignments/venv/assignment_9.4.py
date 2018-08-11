name = input("Enter file:")
handle = open(name)
d = dict()
A = []
for line in handle:
    if(line.startswith('From') and not(line.startswith('From:'))):
        A.append(line.split()[1])
for val in A:
    d[val] = A.count(val)
max_val = max(d.values())
for mail, count in d.items():
    if(count == max_val):
        print(mail,count)
