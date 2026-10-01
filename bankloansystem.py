age=int(input("Enter Your Age: "))
salary=float(input("Enter Your Salary: "))
credit_score=int(input("Enter Your Credit Score: "))
employement=input("Employed or Unemployed: ")
loan=float(input("Enter Loan Amount: "))

print("---Loan Type---")
print("Personal")
print("Bussiness")
print("Education")

loan_type=input("Enter loan tyoe: ").title()

match loan_type:
    case "Personal":
        if age <23:
            print("Minimum Age Required 23.")
        elif salary <50000:
            print("Minimum Salary is 50000")
        elif credit_score<60:
            print("Minimum Credit Score Required 60")
        elif employement != "Employed":
            print("Employment is Complsury")
        elif loan > 100000:
            print("Maximum loan Is 100000")
        else:
            print("Personal Loan is Approved")
            
    case "Bussiness":
        if age <25:
            print("Minimum Age Required 23.")
        elif salary<80000:
            print("Minimum Salary is 80000")
        elif credit_score<60:
            print("Minimum Credit Score Required 60")
        elif employement != "Employed":
            print("Employment is Complsury")
        elif loan > 200000:
            print("Maximum loan Is 200000")
        else:
            print("Business Loan is Approved")
    case "Education":
        if age <16:
            print("Minimum Age Required 23.")
        elif salary<30000:
            print("Minimum Salary is 30000")
        elif credit_score<60:
            print("Minimum Credit Score Required 60")
        elif employement != "Employed":
            print("Employment is Complsury")
        elif loan > 50000:
            print("Maximum loan Is 50000")
        else:
            print("Education Loan is Approved")

    case _:
        print("Invalid Type")

