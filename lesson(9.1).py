####Write a program to check whether the student can take an exam or not. Students will be allowed only in two conditions: If they have a medical cause (‘Y’ for yes and ‘N’ for no). If yes, then they will be allowed. If No, then check attendance If attendance is above 75, then allowed; otherwise, not allowed.
medical_cause=str(input("enter your medical cause.Y or N"))
attendance=int(input("enter your attendence"))

if medical_cause=="Y":
    print("you can enter the test")
else:
    if attendance>=75:
        print("you are able to enter the test")
    else:
        print("chale ja yaan se!!")    
    