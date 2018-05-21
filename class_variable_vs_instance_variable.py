class Girl:

    gender = 'female'

    def __init__(self,name):
        self.name = name

r = Girl("ABC")
s = Girl("PQR")
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)