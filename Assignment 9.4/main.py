name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

senders = dict()

for line in handle:
    line = line.strip().split()

    if len(line) > 0:
        if line[0] == "From":
            email = line[1]
            senders[email] = senders.get(email, 0) + 1

largesender = None
largecount = None

for email,count in senders.items():
    if largesender == None or count > largecount:
        largesender = email
        largecount = count

print(largesender,largecount)