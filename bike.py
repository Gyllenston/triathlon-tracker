with open("bike.log", 'a') as file:  
    myCoolVariable = input("How far did u bike?\n")
    
    file.write(myCoolVariable +"\n")
