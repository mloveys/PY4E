fh = open("romeo.txt")

words = []

for line in fh:
    for word in line.rstrip().split():
        if not word in words:
            words.append(word)

words.sort()

print(words)