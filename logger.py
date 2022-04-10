
def log_run():
    with open("run.log", 'a') as file:  
        myCoolVariable = input("How far did you run\n")
    
        file.write(myCoolVariable +"\n")
        print("good run bro")

def log_swim():
    with open("swim.log", 'a') as file:  
        myCoolVariable = input("How long did u swim?\n")
        file.write(myCoolVariable +"\n")
        print("swim fasta")


def log_bike():
    with open("bike.log", 'a') as file:  
        myCoolVariable = input("How far did u bike?\n")
    
        file.write(myCoolVariable +"\n")
        print("bike man")

#def extra_info(shreklol, kreklockc):
#    print(shreklol, kreklockc)

if __name__ == "__main__":
    print("Hello world!")
    log_swim()
    log_bike()
    log_run()
    #extra_info("semon" , "blood")    



