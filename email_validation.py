email=input("Enter your email address: ")
d,j,k=0,0,0

#### check length of email address #####
if len(email)>=6:
    ### check first index is alphabet or not #####
    if email[0].isalpha():
    #####check @ is or not present in email if yes then only ones times present #####
        if ("@" in email) and (email.count("@")==1):
         #### check domain position #####
            if (email[-4]==".")^(email[-3]=="."):
            ### Looping for cheching space etc #####
                for i in email:
                #### Check space in email or not #####
                    if i == i.isspace():
                        k=1
                #### check alphabet in email ###
                    elif i.isalpha():
                ### check email is in upper or lower case ###
                        if i == i.upper():
                            j=1
                ########## check digit is n email ###
                    elif i.isdigit():
                        continue
                #####  check special characters ###
                    elif i =="_" or i =="@" or  i =="." :
                        continue
                    ##### check other special characters ###
                    else:           
                        d=1
                if k==1 or j==1 or d==1:
                    print("Please enter  in your  email in correct format")
                else:
                    print("Right email")
            else:
                print("Missing domain name in email")
        else:
            print("@ is missing and @ is enter more thsn 1 times")
    else:
        print("email address not starting with  any digits")
else:
    print("Too short email address")