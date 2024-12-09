import random

while True:
    try:
        if (level := int(input("Level: "))) > 0:
            x = random.randint(1, level)
            while True:
                try:
                    if (guess := int(input("Guess: "))) > 0:
                        print("Too small!" if guess < x else "Too large!" if guess > x else "Just right!")
                        if guess == x:
                            break
                except ValueError:
                    pass
            break
    except ValueError:
        pass
