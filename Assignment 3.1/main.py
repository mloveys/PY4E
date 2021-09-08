hours_worked = input("Enter Hours Worked: ")
hours_worked = float(hours_worked)

hourly_rate = input("Enter Hourly Rate: ")
hourly_rate = float(hourly_rate)

total_pay = 0;

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    total_pay = (hourly_rate * 40.0) + (overtime_hours * (hourly_rate * 1.5))
elif hours_worked < 40:
    total_pay = (hourly_rate * hours_worked)

print(total_pay)