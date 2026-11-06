
class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self.age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def display_info(self):
        print(f"Animal name: {self.name}, Health Level: %{self.health_level}, Happiness Level: %{self.happiness_level}")
        return self

    def feed(self):
        self.health_level = min(self.health_level +10, 100)
        self.happiness_level = min(self.happiness_level +10, 100)
        return self

class Lion (Animal):
    def __init__(self, name, age, health_level, happiness_level, speed):
        super().__init__(name, age, health_level, happiness_level)
        self.speed = speed

    def display_info(self):
        super().display_info()
        print(f"speed: %{self.speed}")
        return self
    
    def feed(self):
        super().feed()
        self.speed = min(self.speed +5, 100)
        return self


class Monkey (Animal):
    def __init__(self, name, age, health_level, happiness_level, balance):
        super().__init__(name, age, health_level, happiness_level)
        self.balance = balance

    def display_info(self):
        super().display_info()
        print(f"balance: %{self.balance}")
        return self

    def feed(self):
        super().feed()
        self.balance = min(self.balance +2, 100)
        return self

class Bear (Animal):
    def __init__(self, name, age, health_level, happiness_level, weight):
        super().__init__(name, age, health_level, happiness_level)
        self.weight = weight

    def display_info(self):
        super().display_info()
        print(f"weight: %{self.weight}")
        return self

    def feed(self):
        super().feed()
        self.weight = min(self.weight +8, 100)
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        return self

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)

        for animal in self.animals:
            animal.display_info()
        return self

#Instances

lion1 = Lion ("Simba", 5, 80, 90, 70)
monkey1 = Monkey ("Punch", 3, 75, 85, 0)
bear1 = Bear ("Paddington", 8, 90, 80, 60)

zoo1 = Zoo ("Zootopia")
zoo1.add_animal(lion1).add_animal(monkey1).add_animal(bear1).print_all_info()