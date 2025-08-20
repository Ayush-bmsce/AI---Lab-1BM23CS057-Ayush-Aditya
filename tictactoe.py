import random

def filled(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                return False
    return True

def haswon(arr):
    # rows and cols
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] != 0:  # row
            return arr[i][0]
        if arr[0][i] == arr[1][i] == arr[2][i] != 0:  # col
            return arr[0][i]

    # diagonals
    if arr[0][0] == arr[1][1] == arr[2][2] != 0:
        return arr[0][0]
    if arr[0][2] == arr[1][1] == arr[2][0] != 0:
        return arr[0][2]

    return 'No'

def show(arr):
    for row in arr:
        for item in row:
            if item == 0:
                print('_', end=" ")
            else:
                print(item, end=" ")
        print()
    print()

arra = [[0 for _ in range(3)] for _ in range(3)]

In = input("Enter X or 0 here : ").upper()
comp = '0' if In == 'X' else 'X'

show(arra)

while haswon(arra) == 'No' and not filled(arra):
    # Player move
    i = int(input("Enter x axis (0-2): "))
    j = int(input("Enter y axis (0-2): "))
    while arra[i][j] != 0:
        print("Cell already taken, try again.")
        i = int(input("Enter x axis (0-2): "))
        j = int(input("Enter y axis (0-2): "))

    arra[i][j] = In

    if haswon(arra) != 'No' or filled(arra):
        break

    i1, j1 = random.randint(0, 2), random.randint(0, 2)
    while arra[i1][j1] != 0:
        i1, j1 = random.randint(0, 2), random.randint(0, 2)
    arra[i1][j1] = comp

    show(arra)

winner = haswon(arra)
show(arra)
if winner == In:
    print("Player won ")
elif winner == comp:
    print("Player lost ")
else:
    print("It was a draw ")


    

 
