while(True):
    print("----------------------------")
    print("@@-----BODY MASS INDEX----@@")
    print("----------------------------")
    print("1:BMI 2:Imp BMI 3:exit")
    ch=int(input("enter choice"))
    if ch==1:
        w=float(input("enter weight in kg"))
        h=float(input("enter height in meter"))
        est=(w/(h**2))
        if(est<=17.9):
            print("under weight:",est)
            print("contact m diet expert")
            print("mob:78678787")
        elif(est>=18 and est<=29.9):
                 print("fit:",est)
        
        elif(est>=25 and est<=24.9):
                print("over weight:",est)
                print("contact b gym trainer")
                print("mob:78678787")
        else:
                print("critical")
    elif ch==2:
        w=float(input("enter weight in pounds"))
        h=float(input("enter height in inches"))
        est1=703*w/(h**2)
        if(est<=17.9):
            print("under weight:",est)
            print("contact m diet expert")
            print("mob:78678787")
        elif(est>=18 and est<=29.9):
                 print("fit:",est)
        
        elif(est>=25 and est<=24.9):
                print("over weight:",est)
                print("contact b gym trainer")
                print("mob:78678787")
        else:
                print("critical")
       
    
    elif ch==3:
            break
    else:
        print("invalid choice")
    
        
