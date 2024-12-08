def convert(val):
    y = ""
    for x in val:
        if x == ":)":
            y += " 🙂"
        elif x == ":(":
            y += " 🙁"
        else:
            y += " "+ x
    return y

def main():
    x = input("Enter a prompt - ").split()
    print(convert(x))
    
if __name__ == "__main__":
    main()