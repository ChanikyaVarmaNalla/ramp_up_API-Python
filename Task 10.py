class Animals:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def sound_made(self):
        return f"{self.name} always {self.sound}'s"


class Enclosures:
    def __init__(self, name, section):
        self.name = name
        self.section = section

    def in_area(self):
        return f"{self.name} is kept in {self.section}"


class Lion(Animals):
    def __init__(self, name, section):
        super().__init__("Lion", "Roar")
        self.name = name
        self.section = section


class Elephant(Animals):
    def __init__(self, name, section):
        super().__init__("Elephant", "Trumpet")
        self.name = name
        self.section = section


class Cage(Enclosures):
    def __init__(self, name, section, material):
        super().__init__(name, section)
        self.material = material


# Demonstrate how animals can reside in enclosures
li = Lion("Simba", "section 7")
ele = Elephant("Dumbo", "section 10")
ca1 = Cage("Lion Cage", "section 7", "Iron")
ca2 = Cage("Elephant Sanctuary", "section 10", "Concrete")

print(f"{li.name} is placed in {ca1.name} in {li.section} surrounded by {ca1.material}.")
print(li.sound_made())

print(f"{ele.name} is roaming in {ca2.name} in {ele.section} surrounded by {ca2.material}.")
print(ele.sound_made())
