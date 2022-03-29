def main():
    input_name= str(input("Please enter your credit card type (no spaces, ex:\nAmericanExpress or MasterCard or Visa): "));
    if(isValidName(input_name)):
        print("Card type is valid.")
        input_num= str(input("Please enter your card number (no spaces): "))
        if(isValidNum(input_name, input_num)):
            print("Card length is valid")
            if(isValidPrefix(input_name, input_num)):
                print("Card prefix is valid.")
                if(isValidLuhn(input_num)):
                    print("Card has been validated.")
                else:
                    print("Card number is invalid.")
            else:
                print("Card prefix is invalid.")
        else:
            print("Card length is invalid")
    else:
        print("Card type is invalid.")
    

#Step 1: Check Card Type
def isValidName(name):
    result= False
    if((name == "AmericanExpress") or (name == "MasterCard") or (name =="Visa")):
        result= True

    return result

#Step 2: Check Length
def isValidNum(name,num):
    result=False
    if((len(num)==16 and name == "MasterCard")):
        result=True
    elif (((len(num)==13 or len(num)==16) and name =="Visa")):
        result=True
    elif (len(num)==15 and name == "AmericanExpress"):
        result= True

    return result

#Step 3: Check Prefix
def isValidPrefix(name,num):
    result=False
    if(name== "Visa" and num[0]== "4"):
        result=True
    elif (name == "AmericanExpress" and (num[0:2]=="34" or num[0:2]=="37")):
        result=True
    elif (name== "MasterCard" and (num[0:2]=="51" or num[0:2]=="52"\
          or num[0:2]=="53" or num[0:2]=="54" or num[0:2]=="55")):
          result=True


    return result

#Step 4: Luhn's Algorithm
def isValidLuhn(num):
    reversed_num= ""
    doubled_num=""
    sumOfNum=0

    #reverses credit card number
    for i in range(len(num)-1,-1,-1):
        reversed_num= reversed_num+num[i]


    #doubles digits in odd positions
    temporary=0
    for i in range(0,len(reversed_num),+1):
        if(i % 2 != 0):
            temporary=int(reversed_num[i])*2
            doubled_num+=str(temporary)
        else:
            doubled_num+=reversed_num[i]


    #adds each single digit to produce a sum
    for i in range(0,len(doubled_num),+1):
        sumOfNum+=int(doubled_num[i])

    if(sumOfNum % 10 == 0):
        return True
    else:
        return False


        


if __name__ == "__main__":
    main()