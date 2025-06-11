print("Az Amőba(TicTacToe)")
jatekter = int(input("3 vagy 5 elemű legyen a játék?(3/5)"))
while jatekter != (3 or 5):
    jatekter = int(input("Hibás választás, csak 3 vagy 5 lehet!"))
def haromelem():
    jatekter = input("Hova szeretnéd rakni a jelet?(1,2,3)")
if jatekter == 1:
    print("X00")
elif jatekter == 2:
    print("0X0")
elif jatekter == 3:
    print("00X")

def otelem():
    jatekter = input("Hova szeretnéd rakni a jelet?(1,2,3,4,5)")
if jatekter == 1:
    print("X0000")
elif jatekter == 2:
    print("0X000")
elif jatekter == 3:
    print("00X00")
elif jatekter == 4:
    print("000X0")
elif jatekter == 5:
    print("0000X")

if jatekter == 3:
    haromelem()
elif jatekter == 5:
    otelem()
else:
    print("Nem érvényes játékmód. Válassz újra!")
    
