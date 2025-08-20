room = [
    [0, 0],
    [0, 0]
]

j = 0
# Loop through each row
for row in room:
    for i in range(2):
        if row[i] == 0:   # if dirty
            row[i] = 1   # clean it
            print(f"Quadrant {i + j + 1} has been cleaned")
            print("Current state of the room")
            for r in room:
                print(r)
    j += 2  # jump by 2 because each row has 2 quadrants

print("\nFinal Room State:")
for r in room:
    print(r)

print("\nAll quadrants are clean!")
