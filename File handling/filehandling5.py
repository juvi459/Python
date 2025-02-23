with open("codingal.txt", "w") as file:
    file.write("Hi i Am Penguin I am 1 Year Old")
file.close()

with open("codingal.txt", "r") as file:
    data = file.readlines()
    print("Words in the lines are...")
    for line in data:
        words = line.split()
        print(words)
    file.close()        