class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
        self.throw = 20
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength
        return self
    
    def attack2(self, pirate):
        pirate.health -= self.throw
        print("Throws star")
        return self

    def deathanimation(self):
        if self.health <= 0:
            print("I have died you scoundral")
        elif self.health <= 10:
            print("FINISH HIM")
        else:
            print("I can still stand")