print("Welcome to Madlibs!")

noun1 = input("Noun: ")
creature = input("Creature: ")
adj1 = input("Adjective: ")
noun2 = input("Noun: ")
adj2 = input("Adjective: ")
pronoun = input("Pronoun: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
noun3 = input("Noun: ")

madlib = (f"In a {noun1} in the ground there lived a {creature}. Not a {adj1}, dirty, wet hole, filled with the ends \
of {noun2} and an {adj2} smell, nor yet a dry, bare, sandy hole with {pronoun} in it to \
{verb1} down on or to {verb2}: it was a {creature}-hole, and that means {noun3}.")


print(f"{madlib}")