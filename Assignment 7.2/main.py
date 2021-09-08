# Use the file name mbox-short.txt as the file name

#fn = input("File Name: ")
fn = "mbox-short.txt"
fh = open(fn)

count = 0
confidence = 0

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        score = line.find("0")
        score = float(line[score:])
        
        count = count + 1
        confidence = confidence + score
        
print ("Average spam confidence:", confidence / count)