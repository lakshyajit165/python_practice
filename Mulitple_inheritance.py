<<<<<<< HEAD
class Mario():

    def move(self):
        print('I am moving')

class Shroom():

    def eat_shroom(self):
        print('Now i am big')

class BigMario(Mario,Shroom):
    pass

bm = BigMario()
bm.move()
=======
class Mario():

    def move(self):
        print('I am moving')

class Shroom():

    def eat_shroom(self):
        print('Now i am big')

class BigMario(Mario,Shroom):
    pass

bm = BigMario()
bm.move()
>>>>>>> bf9ec1b50b9a105f9d7e270e398763a0ccb4d098
bm.eat_shroom()