import random
import time


# getting computer's choice
random.seed(int(time.strftime('%S')))
comp_input = random.randint(0,2)



# for drawing accordingly with the choice

def draw(i):
    if(i==0):
        print("""
                  ----------
              ---'       ----)
                        (----)
                        (----)
                        (----)
              ---.___(-----)
                  
        """)
    elif(i==1):
        print("""
                _______________
              ---'      _______)___
                        ___________)
                        ____________)
                        ___________)
               ---.______________)
""")
    elif(i==2):
        print("""
                _______________
              ---'      _______)____
                        ____________)
                        _____________)
                        _______)
               ---.__________)
            
""")
        
        
# for notifying the choices

def notify(user_input,comp_input):
    print("You Chose: ")
    draw(user_input)
    print("Computer Chose: ")
    draw(comp_input)
    
    
# all conditions to analyse with a try catch

try:
    user_input = int(input("Provide 0 for Rock, 1 for Paper, 2 for Scissor: "))
    if(user_input>=0 and user_input<=2):
        if (user_input==comp_input):
            notify(user_input,comp_input)
            print("It's a Draw")
        elif(user_input==0 and comp_input==1):
            notify(user_input,comp_input)
            print("You Loss")
        elif(user_input==1 and comp_input==2):
            notify(user_input,comp_input)
            print("You Loss")
        elif(user_input==2 and comp_input==0):
            notify(user_input,comp_input)
            print("You Loss")
        else:
            notify(user_input,comp_input)
            print("You Win")
    else:
        print("An error occured")
except:
    print("An error occured")