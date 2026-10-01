age=int(input("Enter your age: "))
percentage=float(input("Enter your Intermidiate Percantage: "))
score=float(input("Enter Your Entry Test Score: "))

print("---Avaiable Programs For Admission---")
print("CS")
print("AI")
print("SE")
print("BBA")

Course =input("Enter The  Program You Want To Take The Admission Which Above Mentioned: ").upper()

match Course:
    case "CS":
        if age >=16 and percentage>=60 and score>=50:
            print("Your Eligible For CS")
        elif percentage < 16:
            print("Minimum Age Requird 16")
        elif percentage < 60 :
            print("Minimum Percentage is 60")
        else:
            print("Minimum Test Score Required 50")
    case "AI":
        if age >=16 and percentage>=70 and score>=50:
            print("Your Eligible For AI")
        elif percentage < 16:
            print("Minimum Age Requird 16")
        elif percentage < 70 :
            print("Minimum Percentage is 60")
        else:
            print("Minimum Test Score Required 50")
    case "SE":
        if age >=16 and percentage>=55 and score>=50:
            print("Your Eligible For SE")
        elif percentage < 16:
            print("Minimum Age Requird 16")
        elif percentage < 55 :
            print("Minimum Percentage is 60")
        else:
            print("Minimum Test Score Required 50")
    case "BBA":
        if age >=16 and percentage>=60 and score>=50:
            print("Your Eligible For BBA")
        elif percentage < 16:
            print("Minimum Age Requird 16")
        elif percentage < 60 :
            print("Minimum Percentage is 60")
        else:
            print("Minimum Test Score Required 50")
    

