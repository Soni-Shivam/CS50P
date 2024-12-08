due = 50
try:
    x = int(input("Insert Coin:"))
    if x in [25, 10,5]:
        due = 50 - x
    while (due>0):
        print("Amount Due:", due)
        x = int(input())
        if x in [25, 10,5]:
            due -= x
    if due <=0:
        print("Change Owed:", abs(due))
except:
    print("enter a number please")
