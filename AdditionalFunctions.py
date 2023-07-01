#Function to check if the enter detail in phone number field is a phone Number or not 
def checkPhoneNumber(number):
    n=len(number)
    if(n!=10):
        return False
    for i in number:
        if (not(i.isnumeric())):
            return False
    return True

#Function to check if the password entered has its required things
#contain one upper case, one symbol, one number and maximum length of 8
def checkpassword(password):
    n=len(password)
    if(n<8):
        return False
    uppercase=0
    symbol=0
    number=0
    lowercase=0
    for i in password:
        if(i.isupper()):
            uppercase+=1
        elif(not i.isalnum()):
            symbol+=1
        elif(i.isnumeric()):
            number+=1
        elif(i.islower()):
            lowercase+=1
    if(not lowercase or not uppercase or not symbol or not number):
        return False
    else:
        return True

        





