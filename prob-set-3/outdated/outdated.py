months = [
    "January", "February", "March", "April", "May", "June", 
    "July", "August", "September", "October", "November", "December"
]

while True:
    try:
        x = input("Date: ").strip()
        if "/" in x:
            month, day, year = x.split("/")
            if int(month) > 12 or int(day) > 31:
                raise ValueError
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
        else:
            month_day, year = x.split(", ")
            month, day = month_day.split(" ")
            if int(day) > 31:
                raise ValueError
            month = months.index(month) + 1
            print(f"{year}-{month:02}-{int(day):02}")
            break
    except (ValueError, IndexError):
        pass
    except EOFError:
        break
