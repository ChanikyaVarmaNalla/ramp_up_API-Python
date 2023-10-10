class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def describe(self):
        return f"This is a {self.species} named {self.name}."


class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.category = "Mammal"

    def describe(self):
        return super().describe() + f" It is a {self.category} and can nurse its young."


class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.category = "Bird"

    def describe(self):
        return super().describe() + f" It is a {self.category} and can fly."


class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        self.category = "Reptile"

    def describe(self):
        return super().describe() + f" It is a {self.category} and is cold-blooded."


# Example usage:
if __name__ == "__main__":
    lion = Mammal("Simba", "Lion")
    eagle = Bird("Eddie", "Eagle")
    snake = Reptile("Sammy", "Snake")

    print(lion.describe())
    print(eagle.describe())
    print(snake.describe())
