def main():
    d = convert(input("Enter time"))
    if d >=7 and d <=8:
        print("breakfast time")
    elif d >=12 and d <=13:
        print("lunch time") 
    elif d >=18 and d <=19:
        print("dinner time")  
# added bonus a.m. and p.m. ie 12hr support along with 24hr
def convert(time):
    a,b = time.split(":")
    try:
        b, c = b.split(" ")
    except:
        c = ""
    a = float(a)
    b = float(b)
    if c == "p.m.":
        return (a+12+b/60)
    elif c == "a.m.":
        return (a+b/60)
    else:
        return (a+b/60)


if __name__ == "__main__":
    main()
