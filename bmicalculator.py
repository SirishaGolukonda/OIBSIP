name=input("enter your name:")
w=int(input("enter your weight in kg:"))
h=int(input("enter your height in cm:"))
BMI=(w)/(h/100)**2
print("Your Body Mass Index is",BMI)
if BMI>0:
    if(BMI<=18.5):
        print(name +",you are underweight.")
    elif(BMI<=24.9):
        print(name +",your weight is normal and you are healthy.")
    elif(BMI<=29.9):
        print(name +",you are overweight.")
    elif(BMI<=30.0):
        print(name +",you are obese.")
    elif(BMI<39.9):
        print(name +",you are severly obese.")
    else:
        print(name +",you are morbidly obese.")
else:
        print("ivalid input")        
