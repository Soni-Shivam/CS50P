def main():
    grocery = dict()
    while True:
        try:
            item = input("").lower()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery.update({item: 1})
        except EOFError:
            for item in sorted(grocery):
                print(f"{grocery[item]} {item.upper()}")
            break
        except KeyError:
            pass
main()