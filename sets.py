canöe = {"Nicole", "Zein", "Me", "Drako", "Tim", "Timmeh", "Hannah", "Jayden", "Sam"}

programming = {"Me", "Renuka", "Timmeh", "Sam", "Ray", "Mick", "Max", "Chad", "Dennis"}

print(canöe.union(programming)) # adds both, removes duplicates

print(canöe.intersection(programming)) # only contains items in both sets

print(canöe.difference(programming)) # contains canöe without programming

print(programming.difference(canöe))

print(canöe.symmetric_difference(programming)) # only contains items in only 1 set
