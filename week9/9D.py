def findMax(number):
    number = list(map(int,number))
    number.sort()
    return number[len(number)-1]