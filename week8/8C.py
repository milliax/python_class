appeared_times = 0
letter_to_delete = "None"
number_to_delete = 0

def count(letter):
    global appeared_times
    if letter == letter_to_delete:
        appeared_times += 1
        if appeared_times == number_to_delete:
            return None
        return letter
    else:
        return letter

sentence = input().split()
letter_to_delete = input()
number_to_delete = int(input())

#ans = list(map(count,sentence))
print(*[x for x in list(map(count,sentence)) if x is not None])