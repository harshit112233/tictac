import time #optional 
button=["_","_","_","_","_","_","_","_","_"]  # all are empty initially
valid='''

    ++++++++++++++++++++++++++++
    Please Enter a valid number :
    ++++++++++++++++++++++++++++

    '''                                       # Just a message for entering a valid number 
def check_tie():  #function to check if it is a tie
    a=[]
    [a.append(button[i]) for i in range(0,9)]
    if "_" in a:
        tie=False
    else:
        tie=True
    return tie

def button_solved():  # function to print all the values
    print(button[0],button[1],button[2])
    print(button[3],button[4],button[5])
    print(button[6],button[7],button[8])
button_solved()

def solved():          #function to check the winning team
    if button[0]==button[1]==button[2]=="X" or button[0]==button[1]==button[2]=="O" or button[3]==button[4]==button[5]=="X" or button[3]==button[4]==button[5]=="O" or button[6]==button[7]==button[8]=="X" or button[6]==button[7]==button[8]=="O" or button[0]==button[3]==button[6]=="X" or button[0]==button[3]==button[6]=="O" or button[1]==button[4]==button[7]=="X" or button[1]==button[4]==button[7]=="O" or button[2]==button[5]==button[8]=="X" or button[2]==button[5]==button[8]=="O" or button[0]==button[4]==button[8]=="X" or button[0]==button[4]==button[8]=="O" or button[2]==button[4]==button[6]=="X" or button[2]==button[4]==button[6]=="O":
        winner="True"                                  # to check all the possible ways to solve tictac
    else:
        winner="Auto"
    return winner

a=[1,2,3,4,5,6,7,8,9]
b=["X","O"]
def enter_number():    #function to start the game
    print("Player X turn : ")                          # First turn is of X player 
    number=1
    while solved()!="True" or solved()!="Tie":         # While loop until the game is finished 
        check_tie()
        if check_tie()==True:                          # if it is a tie print this message 
            print('''
            ===============================
            OH IT'S A TIE
            ===============================
            ''')
            break
        elif solved()=="True":                          # If solved shoe you won
            print('''
            ===============================
            Congratulations YOU WON!!!!!
            ===============================
            ''')
            break
        else:
            num=int(input("Enter the number : "))        # integer input number between 1-9
            if check_tie()==True:                        # If there is a tie then break the loop
                break
            else:
                if button[num-1] in b:        # to check if the entered number place is empty or not
                    time.sleep(1.5)
                    print(valid)
                    button_solved()           # to print values 
                    continue
                else:
                    number+=1
                    if num in a:
                        if int(number) % 2==0:  # To check whose turn is this X or O
                            if button[num-1] in b:
                                time.sleep(1.5)        #optional
                                print(valid) 
                                continue
                            else:
                                button[num-1]="X"  # To give value to the number as X
                                button_solved()
                                print("Player O turn : ")
                        else:
                            if button[num-1] in b:  # To check that the number place is empty or not
                                time.sleep(1.5)     #Optional
                                print(valid)        # To print invalid number message
                                continue
                            else:
                                button[num-1]="O"    # To give value to the number as O
                                button_solved()      # To print the values again
                                print("Player X turn : ")
enter_number()
