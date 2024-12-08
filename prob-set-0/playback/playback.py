sentence = input("Enter a sentence - ")
store = sentence.split(" ")
output = ""
for i in range(len(store)):
    output = output + store[i] + "..."
print(output.rstrip("..."))
