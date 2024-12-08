dishes = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0
while 1:
    try:
        item: str = input("Item: ").lower()
        if item in dishes:
            total += dishes[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        break
    except (ValueError, KeyError):
        pass 
