smallest = None
largest = None

# Start Loop until done is received and both smallest and largest have values
while True:
    number = input("Please enter a number: ")
    
    try:
        number = int(number)
    except:
        
        if number == "done":
            if smallest is None or largest is None:
                print("Not Enough Information to determine smallest and largest")
            else:
                print("Maximum is", largest)
                print("Minimum is", smallest)
                break;
        else:
            print("Invalid input")
            continue
    
    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    
    if largest is None:
        largest = number
    elif number > largest:
        largest = number
    