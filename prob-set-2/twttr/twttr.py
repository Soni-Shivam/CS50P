x = input("Input: ")
output = []
for c in x:
    if c not in ("aeiouAEIOU"):
        output.append(c)
print("Output: ", "".join(output))        