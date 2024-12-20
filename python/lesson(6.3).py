#Write a program to calculate the BMI of a person?
#body mass index
#bmi=weight in kgs/(height*height) in meters


weight=float(input("Enter your weight in kgs pls: "))
hieght=float(input("Enter your heightin meters plz:"))

bmi=weight/(hieght*hieght)

print("BMI is ",bmi)


if bmi<=18.4:
    print("you are underweight")

elif bmi<=24.9:
     print("you are healthy")
elif bmi<=34.9:
     print("you are over weight")  
else:
     print("you are obese")       