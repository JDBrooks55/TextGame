

x = 0
name = " "
choice = " "

inv = []



    
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
    if choice == 'new game' or 'n':
        basement()
    elif choice == 'load game':
        print ("\n\n> Still being coded")
        menu()
    elif choice == 'credits':
        print ("\n\n> Everything was made by me")
        menu()
    elif choice == 'exit':
        quit()
    else:
        print ("\n\n> That's not an option. Read the menu asshole")
        menu()
            

def basement():
    #basement description
    print ("\n\n> You wake up in a dark room")
    print ('> "Where am I?"')
    print ("> You can see light coming from up the stairs north of you")
    choice = input (">>> ")
    choice = choice.lower()

    #basement choices
    if choice == 'north' or 'n':
        hallway1()
    elif choice == 'i' or 'inv' or 'inventory':
        print("\n\n")
        print("> Inventory")
        for x in inv:
            print(">", x)
        basement()
    else:
         print ("\n\n> What?")
         basement()

def hallway1():
    #halfway description
    print ("\n\n> You are in a hallway")
    print("> On the east wall you see 2 doors")
    print("> One leads to a bedroom and the other leads to a living room")
    print("> On the west wall you see a door leading to a kitchen")
    print ("> To your north is a door that leads outside")
    choice = input (">>> ")
    choice = choice.lower()
    
    if choice == 'enter bedroom':
        bedroom()
    elif choice == 'enter living room':
        living_room()
     elif choice == 'enter kitchen':
        kitchen()
    
menu()
