sentence = input()

special_characters = [":",".",",","?",";","\""]

for e in special_characters:
    sentence = sentence.replace(e,"")

sentence = sentence.lower()
sentence = sentence.split()

sentence = sorted(sentence)

cumulate = 1
for i in range(len(sentence)-1):
    if sentence[i] == sentence[i+1]:
        cumulate += 1
    else:
        print("{}: {}".format(sentence[i],cumulate))
        cumulate = 1
print("{}: {}".format(sentence[len(sentence)-1],cumulate))
