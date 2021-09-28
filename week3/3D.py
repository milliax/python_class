str = input()

str = str.replace("sqrt(","$\\sqrt{")
str = str.replace(")","}$")

print(str)