from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")


print("ROUND 1")
michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()
print("=3 O.O")
jack_sparrow.attack(michelangelo)
michelangelo.show_stats()

print("ROUND 2")
michelangelo.attack2(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.attack2(michelangelo)
michelangelo.show_stats()

print("ROUND 3")
michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

jack_sparrow.attack2(michelangelo)
jack_sparrow.attack2(michelangelo)
michelangelo.show_stats()