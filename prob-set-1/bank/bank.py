x = input("welcome :").split()
firstletter = (list(x[0]))[0]
if x[0] == "Hello":
    print("$0")
elif firstletter == "H":
    print('$20')
else:
    print("$100")
