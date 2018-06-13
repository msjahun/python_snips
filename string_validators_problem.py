if __name__ == '__main__':
    str = input()
    isnum = False
    isalpha = False
    isdigit = False
    islower = False
    isupper = False
    
    for i in range(len(str)):
        
        
        if (str[i].isalnum()):
            isnum = True
        if (str[i].isalpha()):
            isalpha = True
        if (str[i].isdigit()):
            isdigit = True
        if (str[i].islower()):
            islower = True
        if (str[i].isupper()):
            isupper = True
        
    print (isnum) 
    print (isalpha)
    print (isdigit) 
    print (islower) 
    print (isupper) 

     