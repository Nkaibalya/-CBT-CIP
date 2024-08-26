import random
user=input('''
 start the Game............................
     1.yes
     2.Exit
            ''')
while True:
    
    youcount=0
    compcount=0
    if user=='1':
        while youcount < 5 and compcount < 5:
            try:
                you=int(input('''
                1-Rock
                2-Paper
                3-Scissor
                enter your choice now.................         
                '''))
                l=["Rock","Paper","Scissor"]
                comp=random.choice(l)
                print("Computer Choose :-",comp)
                c=[1,2,3]
                
                if you in c:
                    if comp=="Rock":
                        if you==2:
                            print("You choose :-","Paper")
                            print("You Won....")
                            print('-'*50)
                            youcount+=1
                        elif you==3:
                            print("You choose :-","Paper")
                            print("Computer Won....")
                            print('-'*50)
                            compcount+=1
                        elif you==1:
                            print("You choose :-","Paper")
                            print("Match Draw...")
                            print('-'*50)
                        
                    elif comp=="Paper":
                        if you==3:
                            print("You choose :-","Scissor")
                            print("You Won....")
                            print('-'*50)
                            youcount+=1
                        elif you==1:
                            print("You choose :-","Scissor")
                            print("Computer Won....")
                            print('-'*50)
                            compcount+=1
                        elif you==2:
                            print("You choose :-","Scissor")
                            print("Match Draw...")
                            print('-'*50)
                    elif comp=="Scissor":
                        if you==1:
                            print("You choose :-","Rock")
                            print("You Won....")
                            print('-'*50)
                            youcount+=1
                        elif you==2:
                            print("You choose :-","Rock")
                            print("Computer Won....")
                            print('-'*50)
                            compcount+=1
                        elif you==3:
                            print("You choose :-","Rock")
                            print("Match Draw...")
                            print('-'*50)
                elif you!=c[0] and you!=c[1] and you!=c[2]:
                    print("Invalid Choice, Please Try Again.. ")
            except Exception as e:
                print("Something Went Wrong , Please Try Again")
        print("\nFinally......................\n")
        print("You Got",youcount)
        print("Computer Got",compcount)
        if youcount==compcount:
            print("\nMatch Draw....")
        elif youcount>compcount:
            print("\nCongratulation.....You Won")
            print('-'*50)
        elif youcount<compcount:
            print("\nYou Loose...\n Better Luck Next Time")
            print('-'*50)
        break
    
    elif user=='2':
        print("Game Finished........................")
        break
    else:
        print('You Entered A Wrong Choice, Please Re-start The Game.')
        break