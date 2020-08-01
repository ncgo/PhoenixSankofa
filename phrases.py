#PHRASES INTRO
import random
import 

BlackLivesMatter=1
Feminism=2
Accessibility=3
Latinx=4
Quit=5

def main():
    #welcome!
    choice()
    display_welcome()

    link()

    display_closing()

    
def choice():
    choice= random.randint(1,5) #for now for place of code
    return choice #user 
    
def display_welcome():
    print("Welcome to ConnectMeWith! We will pair you with another Twitter user and share social movement information!")
    print("For this to work your profile must be public!")
    print("Happy learning!")

def link():
    print()
    choice()
    while choice == 5:
        if choice ==1: #BLM, BLack lives matter, rasicsm or anti racism,
            print("here is a great link to start the conversation",)
            Blm_file=open("blm.txt", "r")
            for x in Blm_file:
                print(x)

            Blm_file.close()
                
        
        if choice ==2: #feminism, femicide, womanism, transwomen, incarcerated women
            print("here is a great link to start the conversation", "#link", )
            fem_file=open("blm.txt", "r")
            for x in fem_file:
                print(x)

            fem_file.close()


        elif choice==3: #accessibility, disability, blindness, deafness,
            print("here is a great link to start the conversation", "#link", )

            acc_file=open("blm.txt", "r")
            for x in acc_file:
                print(x)
            acc_file.close()
            
        elif choice==4: #latinx, latine, latinx and lgbtq
            print("here is a great link to start the conversation", "#link", )
            lax_file=open("blm.txt", "r")
            for x in lax_file:
                print(x)

            lax_file.close()

        else:
            print("We understand your choice to pause! We will circle back in a month!")
            break


def display_closing():
    print()
    print("Please feel free to discuss, donate, or circulate the above attachment!")
    print("To Justice! ")
    print()
    print("Love,")
    print("ConnectMeWith Team")
main()
