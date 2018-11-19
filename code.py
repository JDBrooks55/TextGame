

game = 1
name = " "
choice = " "


    
def menu():

    #Welcome and name designation
    print ("\n\nWelcome to 'insert name of game here'")
    print ("What would you like to do?")
    print ("> New Game")
    print ("> Load Game")
    print ("> Credits")
    print ("> Exit")
    choice = input (">>> ")
    choice = choice.lower()
        
    #Menu choices
    if choice == 'new game':
        game()
    elif choice == 'load game':
        print ("\n\n> Still being coded")
    elif choice == 'credits':
        print ("\n\n> Everything was made by me")
    elif choice == 'exit':
        quit()
    else:
           print ("\n\n> That's not an option. Read the menu asshole")
            

def game():
    print ("\n\n> You wake up in a dark room")
    print ('> "Where am I?"')



menu()
