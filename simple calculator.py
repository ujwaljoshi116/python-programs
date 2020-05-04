def simplecalculator():
#--------------------------#Display the Operators------------------------------
    print("")
    print("1:Addtion")
    print("2.Subtarction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Square")
    print("------------------------------------------------------------------")

#--------------------------#Take User input------------------------------------
    ch=int(input("Choose anyone option:"))

#--------------------------#if-elif-else statement----------------------------- 
    if ch==1:
        print("1.Addtion")
        print("--------------------------------------------------------------")
        no1=float(input("Enter your no1:"))
        no2=float(input("Enter your no2:"))
        addres=no1+no2
        print("addtion of your number is=",addres)
        print("--------------------------------------------------------------")

        
    elif ch==2:
        print("2.Subtraction")
        print("--------------------------------------------------------------")
        no1=float(input("Enter your no1:"))
        no2=float(input("Enter your no2:"))
        subres=no1-no2
        print("subtraction of your number is=",subres)
        print("--------------------------------------------------------------")
    elif ch==3:
        print("--------------------------------------------------------------")
        print("3.Multiplication")
        no1=float(input("Enter your no1:"))
        no2=float(input("Enter your no2:"))
        mulres=no1*no2
        print("multiplication of your no is=",mulres)
        print("--------------------------------------------------------------")
    elif ch==4:
        print("--------------------------------------------------------------")
        print("4.Division")
        no1=float(input("Enter your no1:"))
        no2=float(input("Enter your no2:"))
        divres=no1/no2
        print("division of your no is=",divres)
        print("--------------------------------------------------------------")
    elif ch==5:
        print("--------------------------------------------------------------")
        print("5.Square")
        no1=float(input("Enter your no1:"))
        Sq=no1**2
        print("Square of your no is=",Sq)
        print("--------------------------------------------------------------")

    else:
        print("--------------------------------------------------------------")
        print("Invalid,please try again")
#--------------------------#TO continue program in loop------------------------
    simplecalculator()            

#--------------------------#End of program--------------------------------------
simplecalculator()    
