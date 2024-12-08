answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
right = ["forty two", "forty-two", "42"]
if answer in right:
    print("Yes")
else:
    print("No")