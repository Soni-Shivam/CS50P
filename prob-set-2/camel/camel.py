s = input("enter ")
result = [s[0].lower()]
for c in s[1:]:
    if c in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        result.append("_")
        result.append(c.lower())
    else:
        result.append(c.lower())
print("".join(result))    
    

        