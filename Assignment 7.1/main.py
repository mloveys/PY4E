# If accepting input to the file name:
#filename = input("Please enter the file name to read: ")

filename = "words.txt"
filehandle = open (filename, 'r')

for line in filehandle:
    print(line.rstrip().upper())