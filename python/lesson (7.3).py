####Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?

marks1=float(input("enter your marks"))
marks2=float(input("enter your marks"))
marks3=float(input("enter your marks"))
marks4=float(input("enter your marks"))
marks5=float(input("enter your marks"))


average=(marks1+marks2+marks3+marks4+marks5)/5
         
if average >91 and average<100:
    print("A1")
elif average >81 and average<90:
    print("A2")
elif average >71 and average<80:
    print("B1")
elif average >61 and average<70:
    print("B2")
elif average >51 and average<60:
    print("C1")
elif average >41 and average<50:
    print("C2")
elif average >31 and average<40:
    print("D")
elif average >21 and average<30:
    print("E")
else:
    print(" pADHEGA INDIA TOH BADEGA INDI but AGAR TU NAHI PADHEGA TOBHI BADGA INDIA!!!!")
ord(A)