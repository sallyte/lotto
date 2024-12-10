class Lotto:
    def __init__(self,nubers):
        self.numbers= nubers

    def draw(self):
        return self.numbers

    def __str__(self):
        return str(self.numbers)


