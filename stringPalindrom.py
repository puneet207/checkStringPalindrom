def palindromCheck(inputString):
    length = len(inputString) # calculate length of string
    startCount, endCount = 0, (length-1) #Assignment of variables using two pointers startCount adn endCount
    palindromFlag = False
    while(True):
        if(inputString[startCount] == inputString[endCount]): #Matching character by picking Starting and end value
            if((startCount == endCount) or (length/2) == endCount): #check that it reaches to mid of String
                palindromFlag = True
                break
        else:
            break
        startCount += 1
        endCount -= 1

    if(palindromFlag == True):
        print("Congrats!!Given string fulfill creteria of Palindrom")
    else:
        print("Given string does not fulfill creteria of Palindrom")

palindromCheck("ol0lo")
