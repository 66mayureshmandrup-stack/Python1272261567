import re
txt = "apple123"
if re.fullmatch("[a-zA-Z0-9]+",txt):
    print("this string is valid")
else:
    print("this string is invalid")
