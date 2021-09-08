def computepay (hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        print("Invalid hours or rate received")
        return 0;
    
    totalpay = 0
    
    if hours > 40:
        # Standard Pay for first 40 hours
        totalpay = (40 * rate)
        
        # Total Pay is added to Overtime Pay for everything over the first 40 at 1.5x the rate
        totalpay = totalpay + ((hours - 40) * (rate * 1.50))
    else:
        totalpay = hours * rate;
    
    return totalpay

workedhours = input("Enter Hours Worked: ")
hourlyrate = input("Enter Hourly Rate: ")

print("Pay", computepay(workedhours,hourlyrate))