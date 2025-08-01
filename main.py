#just messing around with ternary for fun

class Package:
    def __init__(self, width, height, length, mass):
        self.width = width
        self.height = height
        self.length = length
        self.mass = mass

    def is_bulky(self):
        volume = self.width * self.height * self.length
        return volume >= 1_000_000 or max(self.width, self.height, self.length) >= 150

    def is_heavy(self):
        return self.mass >= 20

    def classify(self):
        bulky = self.is_bulky()
        heavy = self.is_heavy()
        return (
            "REJECTED" if bulky and heavy else
            "SPECIAL" if bulky or heavy else
            "STANDARD"
        )
