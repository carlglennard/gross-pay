from re import X

message = """
Compute Gross Pay of Employee
Programmed by: Carl Glennard
"""
print(message)

#computing base pay per day
rate = 780
hours = int(input("Enter overtime hours: "))
overtime = hours * 128.90

grosspay = (rate + overtime)

#computing deduction for taxes

sss = int(input("Enter SSS contribution: "))
salary = int(input("Enter Salary Loan: "))
pagibig = int(input("Enter Philhealth Contribution: "))

deductions = sss + salary + pagibig

#computing for total pay per month

dayspresent = int(input("Enter total number of days present: "))

totalpay = (grosspay * dayspresent) - deductions

print("Average Grosspay: Php.", grosspay)
print("Total Deductions: Php.", deductions)
print("Net Pay for the Month: Php.", totalpay)

def sector():
    if (totalpay < 13001):
        print("You belong in the poor sector with salary of Php", totalpay)
    elif (totalpay < 20001):
        print("You belong in middle class sector with salary of Php", totalpay)
    elif (totalpay < 35001):
        print("You belong in upper class sector with salary of Php", totalpay)
    elif (totalpay < 100001):
        print("You belong in rich class sector with salary of Php", totalpay)
    else:
        print("You belong in very rich class sector with salary of Php", totalpay)

sector()

    
