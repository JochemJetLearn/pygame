name1 = input("Please enter name of group 1: ")
name2 = input("Please enter name of group 2: ")
name3 = input("Please enter name of group 3: ")

name = (name1, name2, name3)

size1 = input("\nPlease enter size of group 1: ")
size2 = input("Please enter size of group 2: ")
size3 = input("Please enter size of group 3: ")

size = (size1, size2, size3)

points1 = input("\nPlease enter points of group 1: ")
points2 = input("Please enter points of group 2: ")
points3 = input("Please enter points of group 3: ")

points = (points1, points2, points3)

print("\nNames of groups:")
for i in range(3):
    print(f"Group {i+1}: {name[i]}")

print("\nSizes of groups:")
for i in range(3):
    print(f"Group {i+1}: {size[i]}")

print("\nPoints of groups:")
for i in range(3):
    print(f"Group {i+1}: {points[i]}")