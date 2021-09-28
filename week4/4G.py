import re

str = input()
a,b,c = 1,2,3

if str.startswith("https://") and str.endswith("tn.edu.tw") or str.startswith("http://") and str.endswith("tnfsh.tn.edu.tw"):
    print("OK!!")
else:
    print("Invalid web site URL!")