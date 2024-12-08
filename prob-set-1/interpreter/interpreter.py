expression = input("input an expression")
x, y, z = expression.split(" ")
if y == '+':
    print(float(x) + float(z))
elif y == '-':
    print(float(x) - float(z))
elif y == '/':
    print(float(x) / float(z))
elif y == '*':
    print(float(x) * float(z))

