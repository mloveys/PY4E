name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

emailhour = dict()

for line in handle:
    line = line.strip().split()
    
    if len(line) > 0:
        if line[0] == "From":
            hour = line[5].split(":")[0]
            emailhour[hour] = emailhour.get(hour, 0) + 1

for hour,numberofemails in sorted(emailhour.items()):
    print(hour,numberofemails)