
class Backpack:
    def __init__(self, owner, coins=0):
        self.owner = owner
        self.coins = coins

    def add_coins(self, amount):
        self.coins += amount

    def spend_coins(self, amount):
        if self.coins >= amount:
            self.coins -= amount
        else:
            print("Not enough coins")
        return self

    def display(self):
        print(f"{self.owner}'s backpack has {self.coins} coins")
        return self


class Hero:
    def __init__(self, name):
        self.name = name
        self.backpack = Backpack(name)

    def collect(self, amount):
        self.coins += amount
        return self

    def buy_item(self, amount):
        self.backpack.spend_coins(amount)
        return self

    def gift_coins(self, other_hero, amount):
        if self.backpack.coins >= amount:
            other_hero.backpack.add_coins(amount)
        return self


hero1 = Hero("Lina")
hero2 = Hero("Omar")

hero1.collect(50).buy_item(15).gift_coins(hero2, 20)

hero1.backpack.display()
hero2.backpack.display()


# 1. After running the code the first time, I get an "AttributeError: "'Hero' object has no attribute 'coins' ", which 
#... I believe means that I am trying to get to function called "coins" in my hero class but it diesnt exist, it only
#... exist in the backback class. line 28 because "coins" att. belongs in backback class.

# 2. I think the weak prompt did a good job of explaining the issue, but it didnt tell me how to fix it.

# 3. After giving AI a better prompt, it layed everything in a table for my so that its clean and clear, and to the point.
#... It also gave me minimal fixed for me to fix my code.

#original code (line 27-29):
def collect(self, amount):
        self.coins += amount
        return self

#fixed code:
def collect(self, amount):
    self.backpack.coins += amount
    return self

# Fixed: Hero does not have a coins attribute, so we use the associated Backpack object.