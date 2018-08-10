class Enemy:

    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)


jack = Enemy(5)
jones = Enemy(20)

jack.get_energy()
jones.get_energy()  