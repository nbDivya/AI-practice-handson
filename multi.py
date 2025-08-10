class multifunction():
    def oddeven():
        number=int(input("Enter the number"))
        if(number%2==0):
            print("Even number")
            message="Even"
        else:
            print("Odd number")
            message="Odd"
        return message
    
            
    def BMI():
        weight=int(input("Enter the BMI Index:"))
        if(weight<18.5):
            print("underweight")
            message="underweight"
        elif(weight<=25):
            print("Normal weight")
            message="Normal weight"
        else:
            print("Very Overweight")
            message="Over weight"
        return message    
    
    def addition(num1,num2):
        add=num1+num2
        return add