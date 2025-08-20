import random
def filled(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                return False

    return True

def haswon(arr):
    for i in range(len(arr)-1):
        x1, y1 = 0, 0
        x2, y2 = 0, 0
        x3, y3 = 0, 0
        x4, y4 = 0, 0
        for j in range(len(arr)):
            if arr[i][j] == 'X':
                x1 += 1
            elif arr[i][j] == '0':
                x2 += 1
            
            if arr[j][i] == 'X':
                y1 += 1
            elif arr[j][i] == '0':
                y2 += 1


        if arr[i][i] == 'X':
            x3 += 1
        elif arr[i][i] == '0':
            x4 += 1

        if arr[2-i][2-i] == 'X':
            y3 += 1
        elif arr[2-i][2-i] == '0':
            y4 += 1

        if x1 == 3 or y1 == 3 or x3 == 3 or y3 == 3:
            return 'X'
        
        if x2 == 3 or y2 == 3 or x4 == 3 or y4 == 3:
            return '0'

    return 'No'


def show(arr):
    for item in arr:
        for item1 in item:
            if item1 == 0:
                print('_', end = " ")
            else:
                print(item1, end = " ")


        print()


arra = [[0]*3]*3
In = input("Enter X or 0 here : ")
comp = ""
if In == 'X':
    comp = '0'
else:
    comp = 'X'
show(arra)
while haswon(arra) == 'No' and not filled(arra):
    i = int(input("Enter x axis : "))
    j = int(input("Enter y axis : "))
    while arra[i][j] != 0:
        i = int(input("Enter x axis : "))
        j = int(input("Enter y axis : "))

    arra[i][j] = In    

    i1 = random.randint(0, 2)
    j1 = random.randint(0, 2)
    if not filled(arra):
        while arra[i][j] != 0:
            i1 = random.randint(0, 2)
            j1 = random.randint(0, 2)

        arra[i1][j1] = comp


    show(arra)


if haswon(arra) == In:
    print("Player won")

if haswon(arra) == comp:
    print("Player lost")

if haswon(arra) ==  'No' and filled(arra):
    print("It was a draw")   


    

 
