import inflect
names = list()
while True:
    try:
        names.append(input("Name: ").strip().title())
    except EOFError:
        print("Adieu, adieu, to", inflect.engine().join(names))
        break