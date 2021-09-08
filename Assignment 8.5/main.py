fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.split()
       
    # Check Length, Count from and print email
    if len(line) > 0:
        if line[0] == "From":
            count = count + 1
            print(line[1])
            
    # Iterate over words in the line and if from print email
#    for word in line:
#        if word == "From":
#            count = count + 1
#            print(line[1])

print("There were", count, "lines in the file with From as the first word")
