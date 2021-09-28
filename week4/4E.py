a,b,c,d = input().split()

ques = [int(a),int(b),int(c),int(d)]

if ques == [0,1,0,1]:
    print("A")
elif ques == [0,1,1,1]:
    print("B")
elif ques == [0,0,1,0]:
    print("C")
elif ques == [1,1,0,1]:
    print("D")
elif ques == [1,0,0,0]:
    print("E")
else:
    print("F")
