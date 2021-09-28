number = input()

try:
    number = int(number)
    if number >= 0 and number <=100:
        if(number >= 90):
            print("A")
            print("Work hard play hard.")
        elif(number >= 80):
            print("B")
            print("Work hard play hard.")
        elif(number >= 70):
            print("C")
            print("Work hard play hard.")
        elif(number >= 60):
            print("D")
            print("Work hard play hard.")
        else:
            print("E")
            print("Play hard die hard")
    else:
        print("Error!")
except:
    print("-_-")